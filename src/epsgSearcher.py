from ezdxf.addons import iterdxf
from PathCreator import PathCreator
from Point import Point
from epsgSettings import epsgSettings
from helpers.helpers import *
from helpers.texts import epsg_error


class espgSearcher():
    threshold = 5

    def __init__(self, pathCreator: PathCreator):
        self.pathCreator = pathCreator
        self.epsg = epsg_error

    @property
    def filepath(self):
        return self.pathCreator.full_path

    @property
    def data(self):
        types = ['POINT', 'LINE', 'TEXT', 'INSERT', 'MTEXT', 'LWPOLYLINE']
        dxf_data = iterdxf.modelspace(
            self.filepath, types=types)

        if not dxf_data:
            return

        entities = []
        try:
            i = 0
            while i < self.threshold:
                item = next(dxf_data)

                entities = [*entities] + [item]
                i += 1
        except StopIteration:
            pass
        finally:
            del dxf_data

        pts = [Point(elem.dxf.location)
               for elem in entities if elem.dxftype() == 'POINT']

        lines = [Point(elem.dxf.start)
                 for elem in entities if elem.dxftype() == 'LINE']

        polylines = [Point(elem.get_points()[0][:2])
                     for elem in entities if elem.dxftype() == 'LWPOLYLINE']

        objs = [Point(elem.dxf.insert)
                for elem in entities if elem.dxftype() == 'INSERT' or elem.dxftype() == 'TEXT' or elem.dxftype() == 'MTEXT']

        return pts + lines + polylines + objs

    def check_valid_EPSG(self):
        if not self.data:
            return epsg_error
        self.epsg = most_common([epsgSettings(elem).get_EPSG()
                                for elem in self.data])
        return self.epsg
