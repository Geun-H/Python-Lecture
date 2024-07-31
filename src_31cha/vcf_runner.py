from vcf_handle import Vcf

vcf = Vcf()

# rows = vcf.count_variant_rows("sample.ann.vcf.gz")
# print(rows)
# thou = vcf.find_over_qual("sample.ann.vcf.gz", 1000)
# print(thou)

# 헤드에 인덱싱 작업 하는 명령
col2idx = vcf.make_col2idx("sample.ann.vcf.gz")
# print(col2idx)

# rows_qual_1000 = vcf.qual_filter("sample.ann.vcf.gz", 1000, col2idx["QUAL"])
# print(rows_qual_1000)

# tstv_ratio = vcf.ts_tv_ratio("sample.ann.vcf.gz", col2idx)
# print(tstv_ratio)


# gt_counter = vcf.gt_count("sample.ann.vcf.gz")
# print(gt_counter)

data = vcf.count_indel("sample.ann.vcf.gz", col2idx)
print(data)
