from tfx.proto import example_gen_pb2
from tfx.proto import range_config_pb2

input = example_gen_pb2(splits=[
    example_gen_pb2.Input.Split(name='train',
                                pattern='span-{SPAN:2}'),
    example_gen_pb2.Input.Split(name='eval',
                                pattern='span-{SPAN:2}')])
examples = csv_input(input_dir)
example_gen = CsvExampleGen(input=examples,input_config=input,
                            range_config=range)