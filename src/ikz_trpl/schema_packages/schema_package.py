from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import (
    CompositeSystemReference,
    Instrument,
    Measurement,
)
from nomad.metainfo import MEnum, Quantity, SchemaPackage, SubSection

configuration = config.get_plugin_entry_point(
    'ikz_trpl.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()


# class NewSchemaPackage(Schema):
#     name = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     message = Quantity(type=str)

#     def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#         super().normalize(archive, logger)

#         logger.info('NewSchema.normalize', parameter=configuration.parameter)
#         self.message = f'Hello {self.name}!'

"""
Laser	•	Pharos
◦	Wavelength [nm]: 1030
◦	Repetition rate [kHz]: 50
◦	Output power [mW]: 6000
◦	Power at setup [mW]: 1000
◦	State: Running
◦	Optional:
•	Flint
◦	Wavelength [nm]: 1030
◦	Repetition rate [kHz]: 71600
◦	Output power [mW]: 2300
◦	Power at setup [mW]: 100
◦	State: Running
◦	Optional:
•	Orpheus
◦	Wavelength [nm]: 800
◦	Repetition rate [kHz]: 50
◦	Output power [mW]: 200
◦	Power at setup [mW]: 200
◦	State: Running
◦	Optional:
Excitation	•	Spot size h x v [µm²]: 250 x 250
•	Power at sample [mW]: 70
•	Fluence [mJ/cm²]: 5
•	Incidence angle [°]: 45
•	Polarization: p
•	Wavelength [nm]: 515
•	Optional:
Probing	•	Spot size h x v [µm²]: 100 x 100
•	Power at sample [mW]: 1
•	Fluence [mJ/cm²]: 0.1
•	Incidence angle [°]: 21
•	Polarization: s
•	Wavelength [nm]: 1030
•	Optional:
Motor start positions	•	delay
◦	Value: 0
◦	State:
◦	Limits: -100, 850
•	dummy
◦	Value: 0
◦	State:
◦	Limits: -10, 10
•	Shutter pump
◦	Value: 0
◦	State: Closed
◦	Limits: 0,1
•	Shutter probe
◦	Value: 0
◦	State: Closed
◦	Limits: 0,1
•	chopper
◦	Value: 1000
◦	State: Running
◦	Limits: 0,1000
Scan	•	Type: dscan
•	Motors:
◦	Name: delay
◦	Start: -50
◦	Stop: 850
◦	Intervals: 899
•	Integration time: 0
•	Settle time: 1
Measurement device parameters	•	Lock-in amplifier
◦	Phase coarse/fine: 0/0
◦	Sensitivity: A
◦	Time constant: C
◦	Input switch: Current
◦	PLL-locking: Slow
◦	Ref. Thresh.: 2 V (TTL)
•	SPAD
◦	...
•	TCSPC counting card
◦	...

Sample:

Sample ID:	HU2_2536_4
Material and structure:	InP/Si
Description:	Array of InP nanocrystals on Si tips with a pitch of 500 nm
Sample photo:
Environment:
    •	Temperature
    •	Atmosphere
Non-linear crystals	•	BBO
◦	Quantity: 1
◦	Function: Generate second-harmonic pump from Pharos fundamental
◦	Optional information: Thorlabs NLC06
Polarization optics	•	Polarizing beam splitter cube IR
◦	Quantity: 2
◦	Function: Power control
◦	Optional information: Thorlabs PBS253
•	Half-wave plate IR
◦	Quantity: 2
◦	Function: Power control
◦	Optional information: Thorlabs WPH05M-1030
Mirrors	•	Dielectric E03
◦	Quantity: ???
◦	Function: Beam distribution
◦	Optional information: Thorlabs BB1E03
•	Dichroic
◦	Quantity: 1
◦	Function: Reflect second harmonic and filter out fundamental light
◦	Optional information: Thorlabs DLP650
Focusing optics	•	Plano convex 125AB
◦	Quantity: 2
◦	Function: Focusing pump and probe onto the sample
◦	Optional information: Thorlabs LA1986-AB
•	Plano convex 200B
◦	Quantity: 1
◦	Function: First lens of telescope for SHG generation
◦	Optional information: Thorlabs LA1708B
•	Plano convex 100A
◦	Quantity: 1
◦	Function: Second lens of telescope for SHG generation
◦	Optional information: Thorlabs LA1509A
•	Plano convex 50B
◦	Quantity: 1
◦	Function: Focus reflected probe onto the photo-diode
◦	Optional information: Thorlabs LA1131B
Filters	•	ND2
◦	Quantity: 1
◦	Function: Attenuate the probe power in front of the sample
◦	Optional information: Thorlabs ND20A
•	Longpass 1000
◦	Quantity: 1
◦	Function: Filter out second harmonic pump
◦	Optional information: Thorlabs FELH01000


"""


class TRPLInstrument(Instrument):
    type = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    quantity = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )
    function = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    optional_information = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )


class Laser(Instrument):
    # type = Quantity(
    #     type=str,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    #     default='Laser',
    # )
    function = Quantity(
        type=MEnum(['pump/probe', 'probe', 'pump']),
        # a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
        a_eln={'component': 'EnumEditQuantity'},
    )


# class NonLinearCrystal(TRPLInstrument):
#     type = Quantity(
#         type=str,
#         a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
#         default='Non-linear crystal',
#     )


# class PolarizationOptic(TRPLInstrument):
#     type = Quantity(
#         type=str,
#         a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
#         default='Polarization optic',
#     )


# class Mirror(TRPLInstrument):
#     type = Quantity(
#         type=str,
#         a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
#         default='Mirror',
#     )


class MeasurementSetup(ArchiveSection):
    setup = Quantity(
        type=MEnum(['PL', 'TG', 'THz']),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    delay_type = Quantity(
        type=MEnum(['mechanical', 'electronic']),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    data_processing = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    lasers = SubSection(section_def=Laser, repeats=True)
    non_linear_crystals = SubSection(section_def=TRPLInstrument, repeats=True)
    polarization_optics = SubSection(section_def=TRPLInstrument, repeats=True)
    mirrors = SubSection(section_def=TRPLInstrument, repeats=True)
    focusing_optics = SubSection(section_def=TRPLInstrument, repeats=True)
    filters = SubSection(section_def=TRPLInstrument, repeats=True)
    special_components = SubSection(section_def=TRPLInstrument, repeats=True)
    detectors = SubSection(section_def=TRPLInstrument, repeats=True)


class LaserSettings(ArchiveSection):
    laser_name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    laser_reference = Quantity(
        type=Laser,
        a_eln=ELNAnnotation(component=ELNComponentEnum.ReferenceEditQuantity),
    )
    wavelength = Quantity(
        type=float,
        unit='m',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='nm'
        ),
    )
    repetition_rate = Quantity(
        type=float,
        unit='Hz',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='kHz'
        ),
    )
    output_power = Quantity(
        type=float,
        unit='W',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='mW'
        ),
    )
    power_at_setup = Quantity(
        type=float,
        unit='W',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='mW'
        ),
    )
    state = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    optional = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )


class Excitation(ArchiveSection):
    spot_size_h = Quantity(
        type=float,
        unit='meter',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='µm'
        ),
    )
    spot_size_v = Quantity(
        type=float,
        unit='meter',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='µm'
        ),
    )
    power_at_sample = Quantity(
        type=float,
        unit='W',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='mW'
        ),
    )
    fluence = Quantity(
        type=float,
        unit='joule / centimeters**2',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, # defaultDisplayUnit='mJ/cm²'
        ),
    )
    incidence_angle = Quantity(
        type=float,
        unit='°',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    polarization = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    wavelength = Quantity(
        type=float,
        unit='nm',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='nm'
        ),
    )


class Probing(ArchiveSection):
    spot_size_h = Quantity(
        type=float,
        unit='meter',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='µm'
        ),
    )
    spot_size_v = Quantity(
        type=float,
        unit='m',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='µm'
        ),
    )
    power_at_sample = Quantity(
        type=float,
        unit='W',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='mW'
        ),
    )
    fluence = Quantity(
        type=float,
        unit='joule / centimeters**2',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, # defaultDisplayUnit='mJ/cm²'
        ),
    )
    incidence_angle = Quantity(
        type=float,
        unit='°',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    polarization = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    wavelength = Quantity(
        type=float,
        unit='m',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity, defaultDisplayUnit='nm'
        ),
    )
    optional = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )


class MotorStartPositions(ArchiveSection):
    motor_name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    # motor_reference = Quantity(
    #    type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.ReferenceEditQuantity)
    # )
    value = Quantity(
        type=int,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    state = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    lower_limit = Quantity(
        type=int,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    upper_limit = Quantity(
        type=int,
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )

    # delay = Quantity(
    #     type=int,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    #     minValue=-100,
    #     maxValue=850,
    # )
    # dummy = Quantity(
    #     type=int,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    #     minValue=-10,
    #     maxValue=10,
    # )
    # shutter_pump = Quantity(
    #     type=int,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    #     minValue=0,
    #     maxValue=1,
    # )
    # shutter_probe = Quantity(
    #     type=int,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    #     minValue=0,
    #     maxValue=1,
    # )
    # chopper = Quantity(
    #     type=int,
    #     a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    #     minValue=0,
    #     maxValue=1000,
    # )


class Motors(ArchiveSection):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    start = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )
    stop = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )
    intervals = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )


class Scan(ArchiveSection):
    # scan_type = Quantity(
    #     type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    # )
    command = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    motors = SubSection(section_def=Motors)
    integration_time = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )
    settle_time = Quantity(
        type=int, a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity)
    )


# class LockInAmplifier(ArchiveSection):
#     phase_coarse_fine = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     sensitivity = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     time_constant = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     input_switch = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     pll_locking = Quantity(
#         type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
#     )
#     ref_thresh = Quantity(
#         type=int,
#         unit='V',
#         a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
#     )


# class SPAD(ArchiveSection):
#     pass


# class TCSPCCountingCard(ArchiveSection):
#     pass


class MeasurementDeviceParameters(ArchiveSection):
    # lock_in_amplifier = SubSection(section_def=LockInAmplifier)
    # spad = SubSection(section_def=SPAD)
    # tcspc_counting_card = SubSection(section_def=TCSPCCountingCard)

    device_name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    paramters = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )


class MeasurementSettings(ArchiveSection):
    laser = SubSection(section_def=LaserSettings, repeats=True)
    excitation = SubSection(section_def=Excitation)
    probing = SubSection(section_def=Probing)
    motor_start_positions = SubSection(section_def=MotorStartPositions)
    scan = SubSection(section_def=Scan)
    measurement_device_parameters = SubSection(section_def=MeasurementDeviceParameters)


class TRPLSample(CompositeSystemReference):
    material_and_structure = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    sample_photo = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.FileEditQuantity),
        a_browser={'adaptor': 'RawFileAdaptor'},
    )
    environment = Quantity(
        type=MEnum(['Temperature', 'Atmosphere']),
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )
    description = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )


class IKZTRPLScan(Measurement, Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    user = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    data_file = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.FileEditQuantity)
    )

    samples = SubSection(section_def=TRPLSample)

    measurement_settings = SubSection(section_def=MeasurementSettings)
    measurement_setup = SubSection(section_def=MeasurementSetup)

    # def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
    #     super().normalize(archive, logger)

    #     logger.info('NewSchema.normalize', parameter=configuration.parameter)
    #     self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
