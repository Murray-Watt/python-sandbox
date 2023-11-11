# This code demonstrates how more complex versions imports work.
from src.Modules.Basics.RootsSolver import roots as qr
from src.Modules.Basics import RootsSolver as rs

print(qr(1, 11, 1))
print(rs.roots(1, 11, 1))