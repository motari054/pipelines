statistics_gen = tfx.components.StatisticsGen(
    instance_name='Statistics_Generation',
    example=example_gen.Outputs['examples'])