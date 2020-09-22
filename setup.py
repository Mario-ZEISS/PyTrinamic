'''
Created on 30.12.2018

@author: ED
'''
import setuptools
from PyTrinamic.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTrinamic",
    version=__version__,
    author="ED, LK, LH, JM, ..",
    author_email="tmc_info@trinamic.com",
    description="TRINAMIC's Python Technology Access Package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trinamic/PyTrinamic",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "python-can>=3,<4",
        "canopen",
        "pyserial>=3"
    ],
    scripts=[
        "PyTrinamic/examples/evalboards/TMC2041/TMC2041_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2041/TMC2041_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2100/TMC2100_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2100/TMC2100_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2130/TMC2130_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2130/TMC2130_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2160/TMC2160_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2160/TMC2160_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2208/TMC2208_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2208/TMC2208_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2209/TMC2209_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2209/TMC2209_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2224/TMC2224_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2224/TMC2224_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2225/TMC2225_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2225/TMC2225_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2300/TMC2300_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2300/TMC2300_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2590/TMC2590_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2590/TMC2590_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC2660/TMC2660_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC2660/TMC2660_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4331/TMC4331_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4331/TMC4331_eval_TMC2130_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4330/TMC4330_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4330/TMC4330_eval_TMC2160_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4361/TMC4361_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4361/TMC4361_eval_TMC2660_eval_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_adc_offset_calibration.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder_offset_estimation.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6100_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6100_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_ABN_encoder.py",
        "PyTrinamic/examples/evalboards/TMC4671/TMC4671_eval_TMC6200_eval_BLDC_open_loop.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5031/TMC5031_stallGuardDemo.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5041/TMC5041_stallGuardDemo.py",
        "PyTrinamic/examples/evalboards/TMC5062/TMC5062_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5062/TMC5062_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5072/TMC5072_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5072/TMC5072_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5130/TMC5130_MicroStep.py",
        "PyTrinamic/examples/evalboards/TMC5160/TMC5160_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5160/TMC5160_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_shield_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_coolStep_demo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_stallGuard_demo.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_coolStep_demo_min.py",
        "PyTrinamic/examples/evalboards/TMC5160_shield/TMC5160_stallGuard_demo_min.py",
        "PyTrinamic/examples/evalboards/TMC5161/TMC5161_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC5161/TMC5161_rotateDemo.py",
        "PyTrinamic/examples/evalboards/TMC6300/TMC6300_hall_Demo.py",
        "PyTrinamic/examples/evalboards/TMC6300/TMC6300_openloop_Demo.py",
        "PyTrinamic/examples/evalboards/TMC7300/TMC7300_eval_register_dump.py",
        "PyTrinamic/examples/evalboards/TMC7300/TMC7300_rotateDemo.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMC_603/TMC_603_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCC_160/TMCC_160_CANopen_hall_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCC_160/TMCC_160_TMCL_foc_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCC_160/TMCC_160_TMCL_foc_hall_digital_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM_0010_TMCL_OPC_config_check.py",
        "PyTrinamic/examples/modules/TMCM_0010_OPC/TMCM_0010_TMCL_OPC_config_update.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1160/TMCM_1160_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1161/TMCM_1161_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1240/TMCM_1240_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1260/TMCM_1260_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1270/TMCM_1270_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1276/TMCM_1276_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1370/TMCM_1370_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_CANopen_encoder_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_CANopen_encoder_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_CANopen_hall_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1617/TMCM_1617_CANopen_openloop_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1630/TMCM_1630_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_TMCL_encoder_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_TMCL_hall_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_CANopen_encoder_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_CANopen_encoder_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1633/TMCM_1633_CANopen_hall_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_position_abn_abs.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_hall_endstop.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_hall.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_TMCL_rotate_openloop.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_openloop_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_hall_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_HM_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_CSP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_CSV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1636/TMCM_1636_CANopen_encoder_CST_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_encoder_analog_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_encoder_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_hall_digital_input_test.py",
        "PyTrinamic/examples/modules/TMCM_1640/TMCM_1640_TMCL_hall_positioning_test.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_CANopen_encoder_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_CANopen_encoder_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_CANopen_openloop_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_encoder_n_channel.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_limit_switches.py",
        "PyTrinamic/examples/modules/TMCM_1670/TMCM_1670_TMCL_positioning.py",
        "PyTrinamic/examples/modules/TMCM_3110/TMCM_3110_TMCL_rotateDemo.py",
        "PyTrinamic/examples/modules/TMCM_3110/TMCM_3110_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_3110/TMCM_3110_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_6212/TMCM_6212_CANopen_PP_Mode.py",
        "PyTrinamic/examples/modules/TMCM_6212/TMCM_6212_CANopen_PV_Mode.py",
        "PyTrinamic/examples/modules/TMCM_6212/TMCM_6212_TMCL_rotateDemo.py",
        "PyTrinamic/examples/tools/FirmwareUpdate.py",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    zip_safe=False,
)
