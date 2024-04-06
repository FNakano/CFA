#
#	This python code is based on code found in bma4.h and bma4.c by bosch: see copyright notice in bma4.h
#       The python coded that i added is under MIT licence (see license file) - franz schaefer schaefer@mond.at
#
from micropython import const
import time
from ustruct import unpack


BMA4_CHIP_ID_ADDR		 = const(0x00)
BMA4_ERROR_ADDR		= const(0x02)
BMA4_STATUS_ADDR	= const(0x03)

#  AUX/ACCEL DATA BASE ADDRESS REGISTERS 
BMA4_DATA_0_ADDR	= const(0x0A)
BMA4_DATA_8_ADDR	= const(0x12)

# SENSOR TIME REGISTERS
BMA4_SENSORTIME_0_ADDR	= const(0x18)

#  INTERRUPT/FEATURE STATUS REGISTERS
BMA4_INT_STAT_0_ADDR	= const(0x1C)

#  INTERRUPT/FEATURE STATUS REGISTERS
BMA4_INT_STAT_1_ADDR	= const(0x1D)

#  TEMPERATURE REGISTERS
BMA4_TEMPERATURE_ADDR	= const(0x22)

#  FIFO REGISTERS
BMA4_FIFO_LENGTH_0_ADDR		= const(0x24)
BMA4_FIFO_DATA_ADDR			= const(0x26)

#  ACCEL CONFIG REGISTERS
BMA4_ACCEL_CONFIG_ADDR		= const(0x40)

#  ACCEL RANGE ADDRESS
BMA4_ACCEL_RANGE_ADDR		= const(0x41)

#  AUX CONFIG REGISTERS
BMA4_AUX_CONFIG_ADDR		= const(0x44)

#  FIFO DOWN SAMPLING REGISTER ADDRESS FOR ACCEL
BMA4_FIFO_DOWN_ADDR			= const(0x45)

#  FIFO WATERMARK REGISTER ADDRESS
BMA4_FIFO_WTM_0_ADDR		= const(0x46)

#  FIFO CONFIG REGISTERS
BMA4_FIFO_CONFIG_0_ADDR		= const(0x48)
BMA4_FIFO_CONFIG_1_ADDR		= const(0x49)

#  MAG INTERFACE REGISTERS
BMA4_AUX_DEV_ID_ADDR		= const(0x4B)
BMA4_AUX_IF_CONF_ADDR		= const(0x4C)
BMA4_AUX_RD_ADDR			= const(0x4D)
BMA4_AUX_WR_ADDR			= const(0x4E)
BMA4_AUX_WR_DATA_ADDR		= const(0x4F)

#  INTERRUPT ENABLE REGISTERS
BMA4_INT1_IO_CTRL_ADDR		= const(0x53)
BMA4_INT2_IO_CTRL_ADDR		= const(0x54)

#  LATCH DURATION REGISTERS
BMA4_INTR_LATCH_ADDR		= const(0x55)

#  MAP INTERRUPT 1 and 2 REGISTERS
BMA4_INT_MAP_1_ADDR			= const(0x56)
BMA4_INT_MAP_2_ADDR			= const(0x57)
BMA4_INT_MAP_DATA_ADDR		= const(0x58)
BMA4_INIT_CTRL_ADDR			= const(0x59)

#  FEATURE CONFIG RELATED 
BMA4_RESERVED_REG_5B_ADDR		= const(0x5B)
BMA4_RESERVED_REG_5C_ADDR		= const(0x5C)
BMA4_FEATURE_CONFIG_ADDR		= const(0x5E)
BMA4_INTERNAL_ERROR			= const(0x5F)

#  SERIAL INTERFACE SETTINGS REGISTER
BMA4_IF_CONFIG_ADDR		= const(0x6B)

#  SELF_TEST REGISTER
BMA4_ACC_SELF_TEST_ADDR	= const(0x6D)

#  SPI,I2C SELECTION REGISTER
BMA4_NV_CONFIG_ADDR		= const(0x70)

#  ACCEL OFFSET REGISTERS
BMA4_OFFSET_0_ADDR		= const(0x71)
BMA4_OFFSET_1_ADDR		= const(0x72)
BMA4_OFFSET_2_ADDR		= const(0x73)

#  POWER_CTRL REGISTER
BMA4_POWER_CONF_ADDR	= const(0x7C)
BMA4_POWER_CTRL_ADDR	= const(0x7D)

#  COMMAND REGISTER
BMA4_CMD_ADDR		= const(0x7E)

#  GPIO REGISTERS
BMA4_STEP_CNT_OUT_0_ADDR	= const(0x1E)
BMA4_HIGH_G_OUT_ADDR		= const(0x1F)
BMA4_ACTIVITY_OUT_ADDR		= const(0x27)
BMA4_ORIENTATION_OUT_ADDR	= const(0x28)
BMA4_INTERNAL_STAT			= const(0x2A)

BMA4_BLOCK_SIZE			= const(32)

#  I2C slave address 
BMA4_I2C_ADDR_PRIMARY	= const(0x18)
BMA4_I2C_ADDR_SECONDARY	= const(0x19)
BMA4_I2C_BMM150_ADDR    = const(0x10)

#  Interface selection macro 
BMA4_SPI_INTERFACE		= const(1)
BMA4_I2C_INTERFACE		= const(2)

#  Interface selection macro 
BMA4_SPI_WR_MASK		= const(0x7F)
BMA4_SPI_RD_MASK		= const(0x80)

#  Auxiliary sensor selection macro 
BMM150_SENSOR			= const(1)
AKM9916_SENSOR			= const(2)
BMA4_ASIC_INITIALIZED		= const(0x01)

#  Auxiliary sensor chip id macros 
BMM150_CHIP_ID                  = const(0x32)

#  Auxiliary sensor other macros 
BMM150_POWER_CONTROL_REG                = const(0x4B)
BMM150_POWER_MODE_REG			= const(0x4C)

# 	CONSTANTS 
BMA4_FIFO_CONFIG_LENGTH		= const(2)
BMA4_ACCEL_CONFIG_LENGTH	= const(2)
BMA4_FIFO_WM_LENGTH			= const(2)
BMA4_CONFIG_STREAM_SIZE		= const(6144)
BMA4_NON_LATCH_MODE			= const(0)
BMA4_LATCH_MODE				= const(1)
BMA4_OPEN_DRAIN				= const(1)
BMA4_PUSH_PULL				= const(0)
BMA4_ACTIVE_HIGH			= const(1)
BMA4_ACTIVE_LOW				= const(0)
BMA4_EDGE_TRIGGER			= const(1)
BMA4_LEVEL_TRIGGER			= const(0)
BMA4_OUTPUT_ENABLE			= const(1)
BMA4_OUTPUT_DISABLE			= const(0)
BMA4_INPUT_ENABLE			= const(1)
BMA4_INPUT_DISABLE			= const(0)

#  ACCEL RANGE CHECK
BMA4_ACCEL_RANGE_2G		= const(0)
BMA4_ACCEL_RANGE_4G		= const(1)
BMA4_ACCEL_RANGE_8G		= const(2)
BMA4_ACCEL_RANGE_16G	= const(3)

#   CONDITION CHECK FOR READING AND WRTING DATA
BMA4_MAX_VALUE_FIFO_FILTER		= const(1)
BMA4_MAX_VALUE_SPI3				= const(1)
BMA4_MAX_VALUE_SELFTEST_AMP		= const(1)
BMA4_MAX_IF_MODE				= const(3)
BMA4_MAX_VALUE_SELFTEST_SIGN	= const(1)

#  BUS READ AND WRITE LENGTH FOR MAG & ACCEL
BMA4_MAG_TRIM_DATA_SIZE		= const(16)
BMA4_MAG_XYZ_DATA_LENGTH	= const(6)
BMA4_MAG_XYZR_DATA_LENGTH	= const(8)
BMA4_ACCEL_DATA_LENGTH		= const(6)
BMA4_FIFO_DATA_LENGTH		= const(2)
BMA4_TEMP_DATA_SIZE			= const(1)

#  TEMPERATURE CONSTANT 
BMA4_OFFSET_TEMP		= const(23)
BMA4_DEG			= const(1)
BMA4_FAHREN			= const(2)
BMA4_KELVIN			= const(3)

#  DELAY DEFINITION IN MSEC
BMA4_AUX_IF_DELAY			= const(5)
BMA4_BMM150_WAKEUP_DELAY1	= const(2)
BMA4_BMM150_WAKEUP_DELAY2	= const(3)
BMA4_BMM150_WAKEUP_DELAY3	= const(1)
BMA4_GEN_READ_WRITE_DELAY	= const(1)
BMA4_AUX_COM_DELAY			= const(10)

# 	ARRAY PARAMETER DEFINITIONS
BMA4_SENSOR_TIME_MSB_BYTE	= const(2)
BMA4_SENSOR_TIME_XLSB_BYTE	= const(1)
BMA4_SENSOR_TIME_LSB_BYTE	= const(0)
BMA4_MAG_X_LSB_BYTE			= const(0)
BMA4_MAG_X_MSB_BYTE			= const(1)
BMA4_MAG_Y_LSB_BYTE			= const(2)
BMA4_MAG_Y_MSB_BYTE			= const(3)
BMA4_MAG_Z_LSB_BYTE			= const(4)
BMA4_MAG_Z_MSB_BYTE			= const(5)
BMA4_MAG_R_LSB_BYTE			= const(6)
BMA4_MAG_R_MSB_BYTE			= const(7)
BMA4_TEMP_BYTE				= const(0)
BMA4_FIFO_LENGTH_MSB_BYTE	= const(1)

# 	ERROR CODES	
BMA4_OK				= const(0)
BMA4_E_NULL_PTR			= const(1)
BMA4_E_OUT_OF_RANGE		= const(1 << 1)
BMA4_E_INVALID_SENSOR		= const(1 << 2)
BMA4_E_CONFIG_STREAM_ERROR	= const(1 << 3)
BMA4_E_SELF_TEST_FAIL		= const(1 << 4)
BMA4_E_FOC_FAIL			= const(1 << 5)
BMA4_E_FAIL			= const(1 << 6)
BMA4_E_INT_LINE_INVALID		= const(1 << 7)
BMA4_E_RD_WR_LENGTH_INVALID	= const(1 << 8)
BMA4_E_AUX_CONFIG_FAIL		= const(1 << 9)
BMA4_E_SC_FIFO_HEADER_ERR	= const(1 << 10)
BMA4_E_SC_FIFO_CONFIG_ERR	= const(1 << 11)

# 	UTILITY MACROS	
BMA4_SET_LOW_BYTE			= const(0x00FF)
BMA4_SET_HIGH_BYTE			= const(0xFF00)
BMA4_SET_LOW_NIBBLE			= const(0x0F)

# 	FOC RELATED MACROS	
BMA4_ACCEL_CONFIG_FOC		= const(0xB7)


BMA42X_ST_ACC_X_AXIS_SIGNAL_DIFF	= const(400)
BMA42X_ST_ACC_Y_AXIS_SIGNAL_DIFF	= const(800)
BMA42X_ST_ACC_Z_AXIS_SIGNAL_DIFF	= const(400)

#  Self-test: Resulting minimum difference signal in mg for BMA45x 
BMA45X_ST_ACC_X_AXIS_SIGNAL_DIFF	= const(1800)
BMA45X_ST_ACC_Y_AXIS_SIGNAL_DIFF	= const(1800)
BMA45X_ST_ACC_Z_AXIS_SIGNAL_DIFF	= const(1800)

# 	ERROR STATUS POSITION AND MASK
BMA4_FATAL_ERR_MSK		= const(0x01)
BMA4_CMD_ERR_POS		= const(1)
BMA4_CMD_ERR_MSK		= const(0x02)
BMA4_ERR_CODE_POS		= const(2)
BMA4_ERR_CODE_MSK		= const(0x1C)
BMA4_FIFO_ERR_POS		= const(6)
BMA4_FIFO_ERR_MSK		= const(0x40)
BMA4_AUX_ERR_POS		= const(7)
BMA4_AUX_ERR_MSK		= const(0x80)

# 	Maximum number of bytes to be read from the sensor 
BMA4_MAX_BUFFER_SIZE            = const(81)

# 	NV_CONFIG POSITION AND MASK
#    NV_CONF Description - Reg Addr --> (0x70), Bit --> 3 
BMA4_NV_ACCEL_OFFSET_POS	= const(3)
BMA4_NV_ACCEL_OFFSET_MSK	= const(0x08)

# 	MAG DATA XYZ POSITION AND MASK
BMA4_DATA_MAG_X_LSB_POS		= const(3)
BMA4_DATA_MAG_X_LSB_MSK		= const(0xF8)
BMA4_DATA_MAG_Y_LSB_POS		= const(3)
BMA4_DATA_MAG_Y_LSB_MSK		= const(0xF8)
BMA4_DATA_MAG_Z_LSB_POS		= const(1)
BMA4_DATA_MAG_Z_LSB_MSK		= const(0xFE)
BMA4_DATA_MAG_R_LSB_POS		= const(2)
BMA4_DATA_MAG_R_LSB_MSK		= const(0xFC)

#  ACCEL DATA READY POSITION AND MASK
BMA4_STAT_DATA_RDY_ACCEL_POS	= const(7)
BMA4_STAT_DATA_RDY_ACCEL_MSK	= const(0x80)

#  MAG DATA READY POSITION AND MASK
BMA4_STAT_DATA_RDY_MAG_POS	= const(5)
BMA4_STAT_DATA_RDY_MAG_MSK	= const(0x20)

#  ADVANCE POWER SAVE POSITION AND MASK
BMA4_ADVANCE_POWER_SAVE_MSK	= const(0x01)

#  ACCELEROMETER ENABLE POSITION AND MASK
BMA4_ACCEL_ENABLE_POS		= const(2)
BMA4_ACCEL_ENABLE_MSK		= const(0x04)

#  MAGNETOMETER ENABLE POSITION AND MASK
BMA4_MAG_ENABLE_MSK		= const(0x01)

# 	ACCEL CONFIGURATION POSITION AND MASK
BMA4_ACCEL_ODR_MSK			= const(0x0F)
BMA4_ACCEL_BW_POS			= const(4)
BMA4_ACCEL_BW_MSK			= const(0x70)
BMA4_ACCEL_RANGE_MSK			= const(0x03)
BMA4_ACCEL_PERFMODE_POS			= const(7)
BMA4_ACCEL_PERFMODE_MSK			= const(0x80)

# 	MAG CONFIGURATION POSITION AND MASK
BMA4_MAG_CONFIG_OFFSET_POS		= const(4)
BMA4_MAG_CONFIG_OFFSET_LEN		= const(4)
BMA4_MAG_CONFIG_OFFSET_MSK		= const(0xF0)
BMA4_MAG_CONFIG_OFFSET_REG		= BMA4_AUX_CONFIG_ADDR

#  FIFO SELF WAKE UP POSITION AND MASK
BMA4_FIFO_SELF_WAKE_UP_POS	= const(1)
BMA4_FIFO_SELF_WAKE_UP_MSK	= const(0x02)

# 	FIFO BYTE COUNTER POSITION AND MASK
BMA4_FIFO_BYTE_COUNTER_MSB_MSK	= const(0x3F)

# 	FIFO DATA POSITION AND MASK
BMA4_FIFO_DATA_POS		= const(0)
BMA4_FIFO_DATA_MSK		= const(0xFF)

# 	FIFO FILTER FOR ACCEL  POSITION AND MASK
BMA4_FIFO_DOWN_ACCEL_POS		= const(4)
BMA4_FIFO_DOWN_ACCEL_MSK		= const(0x70)
BMA4_FIFO_FILTER_ACCEL_POS		= const(7)
BMA4_FIFO_FILTER_ACCEL_MSK		= const(0x80)

# 	FIFO HEADER DATA DEFINITIONS    
FIFO_HEAD_A					= const(0x84)
FIFO_HEAD_M					= const(0x90)
FIFO_HEAD_M_A				= const(0x94)
FIFO_HEAD_SENSOR_TIME		= const(0x44)
FIFO_HEAD_INPUT_CONFIG		= const(0x48)
FIFO_HEAD_SKIP_FRAME		= const(0x40)
FIFO_HEAD_OVER_READ_MSB		= const(0x80)
FIFO_HEAD_SAMPLE_DROP		= const(0x50)

# 	FIFO HEADERLESS MODE DATA ENABLE DEFINITIONS   
BMA4_FIFO_M_A_ENABLE		= const(0x60)
BMA4_FIFO_A_ENABLE			= const(0x40)
BMA4_FIFO_M_ENABLE			= const(0x20)

# 	FIFO CONFIGURATION SELECTION    
BMA4_FIFO_STOP_ON_FULL		= const(0x01)
BMA4_FIFO_TIME				= const(0x02)
BMA4_FIFO_TAG_INTR2			= const(0x04)
BMA4_FIFO_TAG_INTR1			= const(0x08)
BMA4_FIFO_HEADER			= const(0x10)
BMA4_FIFO_MAG				= const(0x20)
BMA4_FIFO_ACCEL				= const(0x40)
BMA4_FIFO_ALL				= const(0x7F)
BMA4_FIFO_CONFIG_0_MASK		= const(0x03)
BMA4_FIFO_CONFIG_1_MASK		= const(0xFC)

# 	FIFO FRAME COUNT DEFINITION     
FIFO_LSB_CONFIG_CHECK		= const(0x00)
FIFO_MSB_CONFIG_CHECK		= const(0x80)
BMA4_FIFO_TAG_INTR_MASK		= const(0xFC)

# 	FIFO DROPPED FRAME DEFINITION     
AUX_FIFO_DROP				= const(0x04)
ACCEL_AUX_FIFO_DROP			= const(0x05)
ACCEL_FIFO_DROP				= const(0x01)

#  FIFO MAG DEFINITION
BMA4_MA_FIFO_A_X_LSB	= const(8)

#  FIFO sensor time length definitions
BMA4_SENSOR_TIME_LENGTH		= const(3)

#  FIFO LENGTH DEFINITION
BMA4_FIFO_A_LENGTH			= const(6)
BMA4_FIFO_M_LENGTH			= const(8)
BMA4_FIFO_MA_LENGTH			= const(14)

# 	MAG I2C ADDRESS SELECTION POSITION AND MASK
BMA4_I2C_DEVICE_ADDR_POS		= const(1)
BMA4_I2C_DEVICE_ADDR_MSK		= const(0xFE)

#  MAG CONFIGURATION FOR SECONDARY INTERFACE POSITION AND MASK
BMA4_MAG_BURST_MSK			= const(0x03)
BMA4_MAG_MANUAL_ENABLE_POS		= const(7)
BMA4_MAG_MANUAL_ENABLE_MSK		= const(0x80)
BMA4_READ_ADDR_MSK			= const(0xFF)
BMA4_WRITE_ADDR_MSK			= const(0xFF)
BMA4_WRITE_DATA_MSK			= const(0xFF)

# 	OUTPUT TYPE ENABLE POSITION AND MASK
BMA4_INT_EDGE_CTRL_MASK			= const(0x01)
BMA4_INT_EDGE_CTRL_POS			= const(0x00)
BMA4_INT_LEVEL_MASK				= const(0x02)
BMA4_INT_LEVEL_POS				= const(0x01)
BMA4_INT_OPEN_DRAIN_MASK		= const(0x04)
BMA4_INT_OPEN_DRAIN_POS			= const(0x02)
BMA4_INT_OUTPUT_EN_MASK			= const(0x08)
BMA4_INT_OUTPUT_EN_POS			= const(0x03)
BMA4_INT_INPUT_EN_MASK			= const(0x10)
BMA4_INT_INPUT_EN_POS			= const(0x04)

# 	IF CONFIG POSITION AND MASK
BMA4_CONFIG_SPI3_MSK			= const(0x01)
BMA4_IF_CONFIG_IF_MODE_POS		= const(4)
BMA4_IF_CONFIG_IF_MODE_MSK		= const(0x10)

# 	ACCEL SELF TEST POSITION AND MASK
BMA4_ACCEL_SELFTEST_ENABLE_MSK	= const(0x01)
BMA4_ACCEL_SELFTEST_SIGN_POS	= const(2)
BMA4_ACCEL_SELFTEST_SIGN_MSK	= const(0x04)
BMA4_SELFTEST_AMP_POS			= const(3)
BMA4_SELFTEST_AMP_MSK			= const(0x08)

# 	ACCEL ODR          
BMA4_OUTPUT_DATA_RATE_0_78HZ	= const(0x01)
BMA4_OUTPUT_DATA_RATE_1_56HZ	= const(0x02)
BMA4_OUTPUT_DATA_RATE_3_12HZ	= const(0x03)
BMA4_OUTPUT_DATA_RATE_6_25HZ	= const(0x04)
BMA4_OUTPUT_DATA_RATE_12_5HZ	= const(0x05)
BMA4_OUTPUT_DATA_RATE_25HZ		= const(0x06)
BMA4_OUTPUT_DATA_RATE_50HZ		= const(0x07)
BMA4_OUTPUT_DATA_RATE_100HZ		= const(0x08)
BMA4_OUTPUT_DATA_RATE_200HZ		= const(0x09)
BMA4_OUTPUT_DATA_RATE_400HZ		= const(0x0A)
BMA4_OUTPUT_DATA_RATE_800HZ		= const(0x0B)
BMA4_OUTPUT_DATA_RATE_1600HZ	= const(0x0C)

# 	ACCEL BANDWIDTH PARAMETER         
BMA4_ACCEL_OSR4_AVG1		= const(0)
BMA4_ACCEL_OSR2_AVG2		= const(1)
BMA4_ACCEL_NORMAL_AVG4	    = const(2)
BMA4_ACCEL_CIC_AVG8			= const(3)
BMA4_ACCEL_RES_AVG16		= const(4)
BMA4_ACCEL_RES_AVG32		= const(5)
BMA4_ACCEL_RES_AVG64		= const(6)
BMA4_ACCEL_RES_AVG128		= const(7)

# 	ACCEL PERFMODE PARAMETER         
BMA4_CIC_AVG_MODE			= const(0)
BMA4_CONTINUOUS_MODE		= const(1)

# 	MAG OFFSET         
BMA4_MAG_OFFSET_MAX		= const(0x00)

# 	ENABLE/DISABLE SELECTIONS        
BMA4_X_AXIS		= const(0)
BMA4_Y_AXIS		= const(1)
BMA4_Z_AXIS		= const(2)

#  SELF TEST
BMA4_SELFTEST_PASS				= const(0)
BMA4_SELFTEST_FAIL				= const(1)

#  INTERRUPT MAPS    
BMA4_INTR1_MAP		= const(0)
BMA4_INTR2_MAP		= const(1)

# 	INTERRUPT MASKS        
BMA4_FIFO_FULL_INT			= const(0x0100)
BMA4_FIFO_WM_INT			= const(0x0200)
BMA4_DATA_RDY_INT			= const(0x0400)
BMA4_MAG_DATA_RDY_INT		= const(0x2000)
BMA4_ACCEL_DATA_RDY_INT		= const(0x8000)


# 	AKM POWER MODE SELECTION     
AKM_POWER_DOWN_MODE			= const(0)
AKM_SINGLE_MEAS_MODE		= const(1)

# 	SECONDARY_MAG POWER MODE SELECTION    
BMA4_MAG_FORCE_MODE			= const(0)
BMA4_MAG_SUSPEND_MODE		= const(1)

# 	MAG POWER MODE SELECTION    
FORCE_MODE			= const(0)
SUSPEND_MODE		= const(1)

# 	ACCEL POWER MODE    
ACCEL_MODE_NORMAL	= const(0x11)

# 	MAG POWER MODE    
MAG_MODE_SUSPEND		= const(0x18)

# 	ENABLE/DISABLE BIT VALUES    
BMA4_ENABLE			= const(0x01)
BMA4_DISABLE		= const(0x00)

# 	DEFINITION USED FOR DIFFERENT WRITE   
BMA4_MANUAL_DISABLE			= const(0x00)
BMA4_MANUAL_ENABLE			= const(0x01)
BMA4_ENABLE_MAG_IF_MODE		= const(0x01)
BMA4_MAG_DATA_READ_REG		= const(0x0A)
BMA4_BMM_POWER_MODE_REG		= const(0x06)
BMA4_SEC_IF_NULL			= const(0)
BMA4_SEC_IF_BMM150			= const(1)
BMA4_SEC_IF_AKM09916		= const(2)
BMA4_ENABLE_AUX_IF_MODE		= const(0x01)

# 	SENSOR RESOLUTION   
BMA4_12_BIT_RESOLUTION		= const(12)
BMA4_14_BIT_RESOLUTION		= const(14)
BMA4_16_BIT_RESOLUTION      = const(16)

#     MULTIPLIER 
#  for handling micro-g values 
BMA4XY_MULTIPLIER         = const(1000000)
# for handling float temperature values 
BMA4_SCALE_TEMP           = const(1000)
# BMA4_FAHREN_SCALED = 1.8 * 1000 
BMA4_FAHREN_SCALED	  = const(1800)
# BMA4_KELVIN_SCALED = 273.15 * 1000 
BMA4_KELVIN_SCALED	  = const(273150)


########################################### defines specific to BMA423

# Chip ID of BMA423 sensor 
BMA423_CHIP_ID				= const(0x13)

# Sensor feature size 
BMA423_FEATURE_SIZE			= const(64)
BMA423_ANYMOTION_EN_LEN			= const(2)
BMA423_RD_WR_MIN_LEN			= const(2)

# Feature offset address 
BMA423_ANY_NO_MOTION_OFFSET		= const(0x00)
BMA423_STEP_CNTR_OFFSET			= const(0x36)
BMA423_STEP_CNTR_PARAM_OFFSET		= const(0x04)
BMA423_WAKEUP_OFFSET			= const(0x38)
BMA423_TILT_OFFSET			= const(0x3A)
BMA423_CONFIG_ID_OFFSET			= const(0x3C)
BMA423_AXES_REMAP_OFFSET		= const(0x3E)




#************************************************************
#	Remap Axes 
#*************************************************************
BMA423_X_AXIS_MASK			= const(0x03)
BMA423_X_AXIS_SIGN_MASK			= const(0x04)
BMA423_Y_AXIS_MASK			= const(0x18)
BMA423_Y_AXIS_SIGN_MASK			= const(0x20)
BMA423_Z_AXIS_MASK			= const(0xC0)
BMA423_Z_AXIS_SIGN_MASK			= const(0x01)

#*************************************************************
#	Step Counter & Detector 
#*************************************************************
# Step counter enable macros 
#
BMA423_STEP_CNTR_EN_POS			= const(4)
BMA423_STEP_CNTR_EN_MSK			= const(0x10)
BMA423_ACTIVITY_EN_MSK			= const(0x20)

# Step counter watermark macros 
BMA423_STEP_CNTR_WM_MSK			= const(0x03FF)

# Step counter reset macros 
BMA423_STEP_CNTR_RST_POS		= const(2)
BMA423_STEP_CNTR_RST_MSK		= const(0x04)

# Step detector enable macros 
BMA423_STEP_DETECTOR_EN_POS		= const(3)
BMA423_STEP_DETECTOR_EN_MSK		= const(0x08)

# Tilt enable macros 
BMA423_TILT_EN_MSK			= const(0x01)

# Step count output length
BMA423_STEP_CNTR_DATA_SIZE		= const(4)

# Wakeup enable macros 
BMA423_WAKEUP_EN_MSK			= const(0x01)

# Wake up sensitivity macros 
BMA423_WAKEUP_SENS_POS			= const(1)
BMA423_WAKEUP_SENS_MSK			= const(0x0E)

# Tap selection macro 
BMA423_TAP_SEL_POS			= const(4)
BMA423_TAP_SEL_MSK			= const(0x10)

#*************************************************************
#	Any Motion 
#*************************************************************
# Any motion threshold macros 
BMA423_ANY_NO_MOTION_THRES_POS		= const(0)
BMA423_ANY_NO_MOTION_THRES_MSK		= const(0x07FF)

# Any motion selection macros 
BMA423_ANY_NO_MOTION_SEL_POS		= const(3)
BMA423_ANY_NO_MOTION_SEL_MSK		= const(0x08)

# Any motion enable macros 
BMA423_ANY_NO_MOTION_AXIS_EN_POS	= const(5)
BMA423_ANY_NO_MOTION_AXIS_EN_MSK	= const(0xE0)

# Any motion duration macros 
BMA423_ANY_NO_MOTION_DUR_MSK		= const(0x1FFF)

#*************************************************************
#	User macros 
#*************************************************************

# Anymotion/Nomotion axis enable macros 
BMA423_X_AXIS_EN			= const(0x01)
BMA423_Y_AXIS_EN			= const(0x02)
BMA423_Z_AXIS_EN			= const(0x04)
BMA423_ALL_AXIS_EN			= const(0x07)
BMA423_ALL_AXIS_DIS			= const(0x00)

# Feature enable macros for the sensor 
BMA423_STEP_CNTR			= const(0x01)
# Below macros are mutually exclusive 
BMA423_ANY_MOTION			= const(0x02)
BMA423_NO_MOTION			= const(0x04)
BMA423_ACTIVITY				= const(0x08)
BMA423_TILT					= const(0x10)
BMA423_WAKEUP				= const(0x20)

# Interrupt status macros 
BMA423_STEP_CNTR_INT			= const(0x02)
BMA423_ACTIVITY_INT			= const(0x04)
BMA423_TILT_INT				= const(0x08)
BMA423_WAKEUP_INT			= const(0x20)
BMA423_ANY_NO_MOTION_INT		= const(0x40)
BMA423_ERROR_INT			= const(0x80)

# Activity recognition macros 
BMA423_USER_STATIONARY			= const(0x00)
BMA423_USER_WALKING			= const(0x01)
BMA423_USER_RUNNING			= const(0x02)
BMA423_STATE_INVALID			= const(0x03)

# Configuration selection macros 
BMA423_PHONE_CONFIG			= const(0x00)
BMA423_WRIST_CONFIG			= const(0x01)

feature_data={ 
   'step_cntr':  (BMA423_STEP_CNTR_OFFSET+1 , BMA423_STEP_CNTR_EN_MSK),
   'activity':   (BMA423_STEP_CNTR_OFFSET+1 , BMA423_ACTIVITY_EN_MSK),
   'tilt':       (BMA423_TILT_OFFSET,         BMA423_TILT_EN_MSK),
   'wakeup':     (BMA423_WAKEUP_OFFSET,       BMA423_WAKEUP_EN_MSK),
   'no_motion':  (1,                          BMA423_ANY_NO_MOTION_SEL_MSK), 
   'any_motion': (1,                          BMA423_ANY_NO_MOTION_SEL_MSK)
  }   


BMA423_PHONE_SC_PARAM = [ 0x132  , 0x78E6  , 0x84  , 0x6C9C  , 0x07  , 0x7564  , 0x7EAA  , 0x55F  , 0xABE  , 0x55F  , 0xE896  ,
  0x41EF  , 0x01  ,   0x0C  , 0x0C  , 0x4A  , 0xA0  , 0x00  , 0x0C  , 0x3CF0  , 0x100 ,  0x00  , 0x00  , 0x00  , 0x00 ]


# Step counter parameter setting(1-25) for wrist (Default) 
BMA423_WRIST_SC_PARAM = [  0x12D  ,0x7BD4  ,0x13B  ,0x7ADB  ,0x04  ,0x7B3F  ,0x6CCD  ,0x4C3  ,0x985 
   , 0x4C3  ,0xE6EC  ,0x460C  ,0x01  ,0x27  ,0x19  ,0x96  ,0xA0  ,0x01  ,0x0C  ,0x3CF0 
   , 0x100  ,0x01  ,0x03  ,0x01  ,0x0E ] 
   
# BMA423_RW_LEN = const(32)   
BMA423_RW_LEN = const(8)   

class BMA4Error(Exception):
    pass

class BMA4:
    def __init__(self, i2c, address=BMA4_I2C_ADDR_SECONDARY):
        self.address=address
        self.bus=i2c
        self.buffer = bytearray(100)
        self.mv = memoryview(self.buffer)
        self.bytebuf = self.mv[82:83]
        self.wordbuf = self.mv[82:84]
        self.confbuf = self.mv[0:BMA423_RW_LEN]
        self.chip_id= self.read_byte(BMA4_CHIP_ID_ADDR)
        # self.write_byte(BMA4_CMD_ADDR, 0xb6 )
        time.sleep_ms(20)
        

    def write_byte(self, reg, val):
        self.bytebuf[0] = val
        #print("write byte %02x %02x" % (reg,val) )
        self.bus.writeto_mem(self.address, reg, self.bytebuf)

    def read_byte(self, reg):
        self.bus.readfrom_mem_into(self.address, reg, self.bytebuf)
        #print("read byte %02x %02x" % (reg,self.bytebuf[0]) )
        return self.bytebuf[0]
        
    def write_data(self, reg, data):
        #print("write data %02x len=%d " % (reg,len(data)),end=" ")
        #for k in data:
        #   print(hex(k),end=" ")
        #print(".")   
        self.bus.writeto_mem(self.address, reg, data)

    def read_data(self, reg, len):
        self.bus.readfrom_mem_into(self.address, reg, self.mv[0:len])
        return self.mv[0:len]

    def stream_transfer_write(self,data):
        asic_msb= 0xff & ( self.streamindex  // 32 )
        asic_lsb= 0x0f & ( self.streamindex  // 2 )      
        self.write_byte(BMA4_RESERVED_REG_5B_ADDR,asic_lsb)
        self.write_byte(BMA4_RESERVED_REG_5C_ADDR,asic_msb)
        self.write_data(BMA4_FEATURE_CONFIG_ADDR,data)
        self.streamindex += len(data)
        
    def readbit(self,addr,mask,pos):
        return (self.read_byte(addr) & mask )  >> pos    

    def writebit(self,addr,mask,pos,value):
           tmp=self.read_byte(addr)
           if value != 0:
             tmp |= mask
           else:
             tmp &= ~mask
           self.write_byte(addr,tmp)
 
    @property
    def accel_enable(self):
       return self.readbit(BMA4_POWER_CTRL_ADDR,BMA4_ACCEL_ENABLE_MSK,BMA4_ACCEL_ENABLE_POS) 
    
    @accel_enable.setter
    def accel_enable(self,value):
       self.writebit(BMA4_POWER_CTRL_ADDR,BMA4_ACCEL_ENABLE_MSK,BMA4_ACCEL_ENABLE_POS,value)
        
    @property
    def advance_power_save(self):
            return self.read_byte(BMA4_POWER_CONF_ADDR) & BMA4_ADVANCE_POWER_SAVE_MSK
        
    @advance_power_save.setter
    def advance_power_save(self,value):
           pwr=self.read_byte(BMA4_POWER_CONF_ADDR)
           #print("apm is ",pwr,"setting to",value)   
           if value != 0:
             pwr |= BMA4_ADVANCE_POWER_SAVE_MSK
           else:
             pwr &= ~BMA4_ADVANCE_POWER_SAVE_MSK 
           self.write_byte(BMA4_POWER_CONF_ADDR,pwr)
           #print("apm writing ",pwr)  
           time.sleep_ms(1)

    def get_feature_config_start_addr(self):
      self.asic_lsb=self.read_byte(BMA4_RESERVED_REG_5B_ADDR) & 0xf
      self.asic_msb=self.read_byte(BMA4_RESERVED_REG_5C_ADDR)
                
             
    def write_config_file(self,fn):
       self.advance_power_save=0
       asic=self.read_byte(BMA4_INTERNAL_STAT)
       #print("asic status=",asic)
      
       self.write_byte(BMA4_INIT_CTRL_ADDR, 0x0);
    
       self.streamindex=0x0000
       with open(fn,"rb") as f:
          nread=f.readinto(self.confbuf)
          while nread > 0:
            self.stream_transfer_write(self.mv[0:nread])
            nread=f.readinto(self.confbuf)
       time.sleep_ms(10)
       self.write_byte(BMA4_INIT_CTRL_ADDR, 0x01);
       #for i in range(0,5):
       #  time.sleep_ms(50)
       #  asic=self.read_byte(BMA4_INTERNAL_STAT)
       #  print("asic status=",asic)
       time.sleep_ms(160)
       asic=self.read_byte(BMA4_INTERNAL_STAT)
       if asic != BMA4_ASIC_INITIALIZED:
          raise BMA4Error("could not initialize asic %02x" % asic )
       self.advance_power_save=1
       self.get_feature_config_start_addr()
       print("* BMA423 ASIC initialized")

    def read_accel(self):
       bt=self.read_data(BMA4_DATA_8_ADDR,6)
       xyzraw=unpack("<hhh",bt)
       div= 16 if self.resolution==12 else ( 4 if self.resolution==14 else 1 ) 
       xyz=tuple([ value // div for value in xyzraw ] )
       return xyz
       
    def feature_config(self,fconfig):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       index=0
       for word in fconfig:
          msb = 0xff & ( word >> 8 )
          lsb = 0xff % word
          data[index] = lsb
          data[index+1]= msb
          index += 2
       self.write_data(BMA4_FEATURE_CONFIG_ADDR,data)
    
    @property
    def accel_range(self):
       tmp=self.read_byte(BMA4_ACCEL_CONFIG_ADDR + 1) & BMA4_ACCEL_RANGE_MSK
       range= 2 << tmp  # 0 is 2g, 1 is 4G,,, 3 is 8G 
       return range
    
    @staticmethod   
    def bit_length(val):
       cnt=0
       while val != 0:
         cnt+=1
         val >>= 1
       return cnt 
       
    @accel_range.setter   
    def accel_range(self,val):
       range=(self.bit_length(val)-2) & BMA4_ACCEL_RANGE_MSK
       tmp=self.read_byte(BMA4_ACCEL_CONFIG_ADDR + 1) & ~BMA4_ACCEL_RANGE_MSK
       tmp |= range
       self.write_byte(BMA4_ACCEL_CONFIG_ADDR + 1,tmp)
       
    
    @property   
    def step_count(self):
       data=self.read_data(BMA4_STEP_CNT_OUT_0_ADDR, BMA423_STEP_CNTR_DATA_SIZE)
       sc=unpack("<I",data)
       return sc[0]
       
    @property   
    def step_dedect_enabled(self):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       sce=data[BMA423_STEP_CNTR_OFFSET + 1]
       return (sce & BMA423_STEP_DETECTOR_EN_MSK ) >> BMA423_STEP_DETECTOR_EN_POS

    @step_dedect_enabled.setter
    def step_dedect_enabled(self,value):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       tmp=data[BMA423_STEP_CNTR_OFFSET + 1]
       if value != 0:
         #print("step dedect enabled")
         tmp |= BMA423_STEP_DETECTOR_EN_MSK
       else:
         tmp &= ~BMA423_STEP_DETECTOR_EN_MSK
       data[BMA423_STEP_CNTR_OFFSET + 1]=tmp
       self.write_data(BMA4_FEATURE_CONFIG_ADDR,data)


    def feature_enable(self,feature,value=1):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       if not feature in feature_data:
         raise BMA4Error("no such feature %s " % feature ) 
       mask, offset=feature_data[feature]
       tmp=data[offset]
       if feature == 'any_motion':
         if value != 0:
           tmp &= ~mask
         else:
           tmp |= mask
       else:
         if value != 0:
           tmp |= mask
         else:
           tmp &= ~mask
       data[offset]=tmp
       if feature== 'any_motion' or feature=='no_motion':
          data[3] =  data[3] & ( ~BMA423_ANY_NO_MOTION_AXIS_EN_MSK)
       self.write_data(BMA4_FEATURE_CONFIG_ADDR,data)

    def feature_anymotion_axis(self,axis):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, 3)
       tmp=data[3]
       tmp &= (~BMA423_ANY_NO_MOTION_AXIS_EN_MSK)
       for i,a in enumerate(['x','y','z']):
          if a in axis:
            tmp |= 1 << (BMA423_ANY_NO_MOTION_AXIS_EN_POS + i)
       self.write_data(BMA4_FEATURE_CONFIG_ADDR,3)



    @property   
    def step_watermark(self):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       wmlsb=data[BMA423_STEP_CNTR_OFFSET]
       wmmsb=data[BMA423_STEP_CNTR_OFFSET+1]
       wm= ( wmlsb + (wmmsb << 8 ) ) & BMA423_STEP_CNTR_WM_MSK 
       return wm

    @step_watermark.setter
    def step_watermark(self,value):
       data=self.read_data(BMA4_FEATURE_CONFIG_ADDR, BMA423_FEATURE_SIZE)
       wmlsb=data[BMA423_STEP_CNTR_OFFSET]
       wmmsb=data[BMA423_STEP_CNTR_OFFSET+1]
       wm= ( wmlsb + (wmmsb << 8 ) ) & ~BMA423_STEP_CNTR_WM_MSK 
       wm |= ( value & BMA423_STEP_CNTR_WM_MSK)
       
       data[BMA423_STEP_CNTR_OFFSET] = wm & 0xff
       data[BMA423_STEP_CNTR_OFFSET + 1] = ( wm >> 8 ) & 0xff
       self.write_data(BMA4_FEATURE_CONFIG_ADDR,data)
       
    def int_status(self):
       is0=self.read_byte(BMA4_INT_STAT_0_ADDR)
       is1=self.read_byte(BMA4_INT_STAT_1_ADDR)
       return (is0,is1)
       
    def map_int(self,line,int,unmap=False):
       addr=[BMA4_INT_MAP_1_ADDR,BMA4_INT_MAP_2_ADDR][line]
       val=self.read_byte(addr)
       map= int & 0xff
       val &= ~map
       if not unmap:
         val |= int
       self.write_byte(addr,val)
       
       
       

class BMA423(BMA4):
        def __init__(self, i2c, address=BMA4_I2C_ADDR_SECONDARY):
            super(BMA423,self).__init__(i2c,address)
            if self.chip_id != BMA423_CHIP_ID:
                raise BMA4Error("chip id should be %02x instead of %02x" % (BMA423_CHIP_ID,self.chip_id) )
            else:
                print("* BMA423 dedected")
                self.resolution = 12
                self.feature_len = BMA423_FEATURE_SIZE
                self.variant = 1
                self.write_config_file()
                self.feature_config(BMA423_WRIST_SC_PARAM)
                self.write_byte(BMA4_INT1_IO_CTRL_ADDR,5) # level trigger, output enable
                self.write_byte(BMA4_INT2_IO_CTRL_ADDR,5)
                self.write_byte(BMA4_INTR_LATCH_ADDR,BMA4_LATCH_MODE)

        def write_config_file(self,fn="bma423.fw"):
            super(BMA423,self).write_config_file(fn)



       
