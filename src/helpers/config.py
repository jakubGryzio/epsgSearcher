import json
import pandas as pd
from .texts import *
from Point import Point

config = pd.read_excel(
    '../Config/Config.xlsx')

EPSG_3120 = config[config['KOD_EPSG'] ==
                   'EPSG3120'].iloc[:, 1:3]  # układ 65 strefa 1
EPSG_2172 = config[config['KOD_EPSG'] ==
                   'EPSG2172'].iloc[:, 1:3]  # układ 65 strefa 2
EPSG_2173 = config[config['KOD_EPSG'] ==
                   'EPSG2173'].iloc[:, 1:3]  # układ 65 strefa 3
EPSG_2174 = config[config['KOD_EPSG'] ==
                   'EPSG2174'].iloc[:, 1:3]  # układ 65 strefa 4
EPSG_2175 = config[config['KOD_EPSG'] ==
                   'EPSG2175'].iloc[:, 1:3]  # układ 65 strefa 5
EPSG_2176 = config[config['KOD_EPSG'] ==
                   'EPSG2176'].iloc[:, 1:3]  # układ 2000 strefa 5
EPSG_2177 = config[config['KOD_EPSG'] ==
                   'EPSG2177'].iloc[:, 1:3]  # układ 2000 strefa 6
EPSG_2178 = config[config['KOD_EPSG'] ==
                   'EPSG2178'].iloc[:, 1:3]  # układ 2000 strefa 7
EPSG_2179 = config[config['KOD_EPSG'] ==
                   'EPSG2179'].iloc[:, 1:3]  # układ 2000 strefa 8
EPSG_2180 = config[config['KOD_EPSG'] == 'EPSG2180'].iloc[:, 1:3]  # układ 1992

# lists of referencial points from config file
EPSG_3120Points = list(map(lambda elem: Point(elem), zip(
    EPSG_3120['Y_GEOD'].tolist(), EPSG_3120['X_GEOD'].tolist())))

EPSG_2172Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2172['Y_GEOD'].tolist(), EPSG_2172['X_GEOD'].tolist())))

EPSG_2173Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2173['Y_GEOD'].tolist(), EPSG_2173['X_GEOD'].tolist())))

EPSG_2174Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2174['Y_GEOD'].tolist(), EPSG_2174['X_GEOD'].tolist())))

EPSG_2175Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2175['Y_GEOD'].tolist(), EPSG_2175['X_GEOD'].tolist())))

EPSG_2176Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2176['Y_GEOD'].tolist(), EPSG_2176['X_GEOD'].tolist())))

EPSG_2177Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2177['Y_GEOD'].tolist(), EPSG_2177['X_GEOD'].tolist())))

EPSG_2178Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2178['Y_GEOD'].tolist(), EPSG_2178['X_GEOD'].tolist())))

EPSG_2179Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2179['Y_GEOD'].tolist(), EPSG_2179['X_GEOD'].tolist())))

EPSG_2180Points = list(map(lambda elem: Point(elem), zip(
    EPSG_2180['Y_GEOD'].tolist(), EPSG_2180['X_GEOD'].tolist())))

# referencial points for układ 65
ref_3120 = EPSG_3120Points[-1]
ref_2172 = EPSG_2172Points[-1]
ref_2173 = EPSG_2173Points[-1]
ref_2174 = EPSG_2174Points[-1]

refs_65 = {epsg_3120: ref_3120, epsg_2172: ref_2172,
           epsg_2173: ref_2173, epsg_2174: ref_2174}

# first digit of Y-coord in PUWG2000
yFirstDigit2176 = '5'
yFirstDigit2177 = '6'
yFirstDigit2178 = '7'
yFirstDigit2179 = '8'

EXCLUDED_DXF_FILE = ['s.DXF', 'S.DXF', 's.dxf', 'S.dxf', 'z.DXF',
                     'Z.DXF', 'z.dxf', 'Z.dxf', 'x.DXF', 'X.DXF', 'x.dxf', 'X.dxf']

EXCLUDED_DWG_FILE = ['s.DWG', 'S.DWG', 's.dwg', 'S.dwg', 'z.DWG',
                     'Z.DWG', 'z.dwg', 'Z.dwg', 'x.DWG', 'X.DWG', 'x.dwg', 'X.dwg']

with open('../Config/config.json') as config_json:
    paths = json.load(config_json)['paths']

OUTPUT_DWG_FOLDER_PATH = paths['output_dwg_folder']
EXCEL_LOG_FILE_PATH = paths['excel_log_file']
LOG_FILE_PATH = paths['log_file']
EXCEL_CONFIG_FILE_PATH = paths['excel_config_file']
