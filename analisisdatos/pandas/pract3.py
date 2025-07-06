import pandas as pd

data = {
    'Producto': ['Manzanas', 'Plátanos', 'Uvas', 'Naranjas', 'Fresas'],
    'Ventas': [150, 200, 75, 300, 90],
    'Precio_kg': [2.5, 1.8, 3.2, 2.0, 4.5],
    'Costo_kg': [1.2, 0.9, 2.0, 1.0, 2.5]
}
df = pd.DataFrame(data)
print(df['Ventas'].std())
#desmotracion de uso de loc
print(df.loc[df['Ventas'] > 100, 'Producto'])
#otra demostracion solo muetra los productos que su precio por kilo es menor a 3.0
print(df.loc[df['Precio_kg']< 3.0, 'Producto'])
