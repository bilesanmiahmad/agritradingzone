KILOS = 'KG'
TONNES = 'MT'
POUNDS = 'LBS'


BIN = 'BIN'
BAG = 'BAG'
CARTON = 'CARTON'
BBAG = 'BBAG'
PBAG = 'PBAG'
SSACK = 'SSACK'
TIN = 'TIN'
PLBAG = 'PLBAG'
BOX = 'BOX'


CMR = 'CMR'
QUALITY_CERTIFICATE = 'QC'
EXPORT_DECLARATION = 'ED'

ORIGIN = 'ORIGIN'
SPOT = 'SPOT'

ORG = 'ORG'
CONV = 'CONV'


METRIC = (
    (KILOS, 'Kilogram'),
    (TONNES, 'Metric Tonnes'),
    (POUNDS, 'Pounds')
)

PACKAGES = (
    (BIN, 'BINS'),
    (BAG, 'BAGS'),
    (CARTON, 'CARTONS'),
    (BBAG, 'BIG BAGS'),
    (PBAG, 'POLY BAGS'),
    (SSACK, 'SUPER SACKS'),
    (TIN, 'TINS'),
    (PLBAG, 'PLASTIC BAGS'),
    (BOX, 'BOXES')
)

DOCUMENTS = (
    (CMR, 'CMR'),
    (QUALITY_CERTIFICATE, 'QUALITY CERTIFICATE'),
    (EXPORT_DECLARATION, 'EXPORT DECLARATION')
)

CROP_TYPE = (
    (ORG, 'Organic'),
    (CONV, 'Conventional')
)

TRANSPORT_METHOD = (
    (ORIGIN, 'Origin'),
    (SPOT, 'Spot')
)
