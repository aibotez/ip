import gc


for x in locals().keys():
    del locals()[x]
gc.collect()