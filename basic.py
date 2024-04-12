basic_config = example_gen_pb2.Output(
    split_config=example_gen_pb2.SplitConfig(splits =[
        example_gen_pb2.SplitConfig.Split(name='train', hash_buckets=4),
        example_gen_pb2.SplitConfig.Split(name='dev' hash_buckets=1)
    ]))
example_gen = tfx.components.CsvExampleGen(
    instance_name ='Data_Extraction_Spliting',
    input=external_input(DATA_ROOT),
    output_config=output_config
    output_config=output_config
)