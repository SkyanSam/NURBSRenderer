import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc
import string as s


def load(filename):
    with open(filename) as f:

        vs = []

        parsingCurve = False
        isRational = False
        ps = []
        ks = []
        u0 = 0
        u1 = 0
        deg = 0

        for line in f:
            line = s.rstrip(line)

            if not line or s.find(line, "#") == 0:
                continue

            while s.rfind(line, "\\") != -1:
                line = s.split(line, "\\")[0]
                nextLine = f.readline()
                if nextLine:
                    line = line + s.strip(nextLine)

            parts = s.split(line)

            if parts[0] == "v":
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                w = 1.0
                if len(parts) > 4:
                    w = float(parts[4])
                vs.append(rg.Point4d(x, y, z, w))

            elif parts[0] == "p":
                idx = int(parts[1]) - 1
                sc.doc.Objects.AddPoint(rg.Point3d(vs[idx]))

            elif parts[0] == "cstype":
                if parts[1] == "rat" and parts[2] == "bspline":
                    parsingCurve = True
                    isRational = True
                elif parts[1] == "bspline":
                    parsingCurve = True

            elif parts[0] == "deg":
                deg = int(parts[1])

            elif parts[0] == "curv":
                u0 = float(parts[1])
                u1 = float(parts[2])
                for i in range(3, len(parts)):
                    idx = int(parts[i]) - 1
                    ps.append(vs[idx])

            elif parts[0] == "parm" and parts[1] == "u":
                for i in range(2, len(parts)):
                    ks.append(float(parts[i]))

            elif parts[0] == "end" and parsingCurve:
                curve = rg.NurbsCurve(3, isRational, deg + 1, len(ps))
                for i in range(len(ps)):
                    curve.Points.SetPoint(i, ps[i])
                for i in range(curve.Knots.Count):
                    # Rhino skips the first and last knot
                    # compared to .obj
                    curve.Knots[i] = ks[i + 1]
                if curve.IsValid:
                    sc.doc.Objects.AddCurve(curve);

                parsingCurve = False
                isRational = False
                ps = []
                ks = []

        sc.doc.Views.Redraw()


if (__name__ == "__main__"):
    filename = rs.OpenFileName(title="Open Obj", filter="OBJ|*.obj||")
    if filename:
        load(filename)