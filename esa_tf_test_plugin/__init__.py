import logging

logger = logging.getLogger("esa_tf_test_plugin")


def run_processing(
    product_path,
    *,
    workflow_options,
    processing_dir,
    output_dir,
):
    logger.info("start test plugin processing")
    return product_path


plugin_definition = {
    "WorkflowName": "test plugin",
    "Description": "dummy plugin for testing esa_tf plugins interface",
    "Execute": "esa_tf_test_plugin.run_processing",
    "InputProductType": "S2MSI1C",
    "OutputProductType": "S2MSI1C",
    "WorkflowVersion": "0.1",
    "WorkflowOptions": {
        "mandatory_parameter": {
            "Description": "mandatory parameter",
            "Type": "boolean",
        },
        "optional_parameter_1": {
            "Description": "first optional parameter",
            "Type": "integer",
            "Default": 1,
        },
        "optional_parameter_2": {
            "Description": "second optional parameter",
            "Type": "string",
            "Default": "one",
            "Enum": ["one", "two"],
        }
    }
}
