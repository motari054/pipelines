example_validator = Example_Validator(
    statistics=Statistics_gen.outputs['statistics'],
    schema=schema_importer.outputs['result'],
    instance_name= 'Data_Validation'
)