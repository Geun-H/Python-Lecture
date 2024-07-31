import gzip


class Vcf:
    def __init__(self):
        self.purine = {"A", "G"}
        self.pyrimidin = {"T", "C"}

    # header에 인덱스 붙이기
    def make_col2idx(self, vcf_filepath):
        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#CHROM"):
                    header = line.strip().split("\t")
                    break
        col2idx = dict(zip(header, range(len(header))))
        return col2idx

    def count_variant_rows(self, vcf_filepath: str):
        cnt = 0
        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#"):
                    continue

                cnt += 1
        return cnt

    # Qual의 index 사용
    def find_over_qual(self, vcf_filepath, qual_criteria):
        cnt = 0
        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#"):
                    continue

                row = line.strip().split("\t")

                if float(row[5]) > qual_criteria:
                    cnt += 1
        return cnt

    # Qual자체의 위치를 찾아서 보려고 (맨 위 함수 이용)
    def qual_filter(self, vcf_filepath, qual_criteria, qual_idx):
        cnt = 0
        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#"):
                    continue

                row = line.strip().split("\t")

                if float(row[qual_idx]) >= qual_criteria:
                    cnt += 1
        return cnt

    # REF 와 ALT의 TS, TV 비율(피리미딘>퓨린:transversion / 같은거로:Transition)
    def ts_tv_ratio(self, vcf_filepath, col2idx):
        ts, tv = 0, 0

        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#"):
                    continue

                row = line.strip().split("\t")
                ref = row[col2idx["REF"]]
                alt = row[col2idx["ALT"]]

                if len(ref) == 1 and len(alt) == 1:
                    if ref in self.pyrimidin and alt in self.pyrimidin:
                        ts += 1
                    elif ref in self.purine and alt in self.purine:
                        ts += 1
                    else:
                        tv += 1

        tstv_ratio = round(ts / tv, 4)  # round(a,*) 반올림, 소수점으로도 이용 가능
        return tstv_ratio

    # GT를 카운트하는
    def gt_count(self, vcf_filepath):
        with gzip.open(vcf_filepath, "rt") as handle:
            gt_data = {}

            for line in handle:
                if line.startswith("#"):
                    continue

                row = line.strip().split("\t")
                gt = row[-1].split(":")[0].replace("|", "/")

                if gt not in gt_data:
                    gt_data[gt] = 0

                gt_data[gt] += 1

            return gt_data

    # 인델 길이 구하기
    def count_indel(self, vcf_filepath, col2idx):
        ins_max, del_max = 0, 0
        with gzip.open(vcf_filepath, "rt") as handle:
            for line in handle:
                if line.startswith("#"):
                    continue

                row = line.strip().split("\t")
                ref = row[col2idx["REF"]]
                alts = row[col2idx["ALT"]].split(",")

                for alt in alts:
                    if len(ref) > len(alt):  # DEL
                        del_len = len(ref) - len(alt)
                        if del_max < del_len:
                            del_max = del_len
                    elif len(ref) < len(alt):
                        ins_len = len(alt) - len(ref)
                        if ins_max < ins_len:
                            ins_max = ins_len

        return {"ins_max": ins_max, "del_max": del_max}
