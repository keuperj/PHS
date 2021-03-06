def main():
    import phs.parameter_definition  # standalone import
    import phs.experiment_definition  # standalone import
    import phs.compute_definition  # standalone import
    # Make sure that python can import 'phs'.
    # One way is to run the 'install.sh' script provided within this project.

    # import CarmeModules.HyperParameterSearch.phs.parallel_hyperparameter_search as phs  # import on Carme
    pardef = phs.parameter_definition.ParameterDefinition()

    pardef.set_data_types_and_order([('x', float), ('f', 'expr'), ('iterations', int), ('s', str)])

    pardef.add_individual_parameter_set(
        number_of_sets=3,
        set={'x': {'type': 'random', 'bounds': [-5, 5], 'distribution': 'uniform', 'round_digits': 3},
             'f': {'type': 'random_from_list', 'lst': ['math.sin(x)', 'math.cos(x)', 'math.tan(x)']},
             'iterations': {'type': 'random', 'bounds': [1, 7], 'distribution': 'uniform', 'round_digits': 0},
             's': {'type': 'random_from_list', 'lst': ['string1', 'string2', 'string3']}},
        prevent_duplicate=True)

    expdef = phs.experiment_definition.ExperimentDefinition(
        experiment_dir='/absolute/path/to/not/yet/existing/folder/your/experiments/should/be/saved',
        target_module_root_dir='/absolute/path/to/root/dir/in/which/your/test_function/resides',
        target_module_name='file_name_with_test_function_definition_(without_extension)',
        target_function_name='data_types_and_order_func',
        parameter_definitions=pardef.get_parameter_definitions())

    compdef = phs.compute_definition.ComputeDefinition(
        experiment_dir='/absolute/path/to/folder/with/existing/experiment',
        parallelization='local_processes',
        local_processes_num_workers=1,
        redirect_stdout=True)

    compdef.start_execution()


if __name__ == "__main__":
    main()
