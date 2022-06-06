import logging
import os

logger = logging.getLogger("esa_tf_test_plugin")


def run_processing(
    product_path,
    *,
    workflow_options,
    processing_dir,
    output_dir,
):
    """
    Execute the processing and return the path of the output product.

    :param str product_path: path of the main Sentinel-2 L1C product folder
    :param dict workflow_options: the user's options dictionary
    :param str processing_dir: path of the processing directory
    :param str output_dir: output directory where to store the output file


    :return str: output path
    """

    logger.info(
        f"start test plugin processing in {processing_dir} "
        f"with workflow_options: {workflow_options}"
    )

    output_path = os.path.join(output_dir, os.path.basename(os.path.normpath(product_path)))
    os.rename(product_path, output_path)
    return output_path


workflow_description = {
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
