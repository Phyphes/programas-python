import os

class Jugador:
    def __init__(self, nombre, añonac, sexo, becado):
        self.nombre = nombre
        self.añonac = añonac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        return f"Nombre: {self.nombre:<20} AñoNac: {self.añonac:<6} Sexo: {'Mujer' if self.sexo == 'M' else 'Hombre':<8} Becado: {'Becado' if self.becado == 1 else 'Sin Beca'}" 

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = list()

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def subtotal(self):
        total = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                total += self.costo
        return total

    def total_hombres_mujeres(self):
        total_hombres = sum(1 for jugador in self.jugadores if jugador.sexo == 'H' and not jugador.becado)
        total_mujeres = sum(1 for jugador in self.jugadores if jugador.sexo == 'M' and not jugador.becado)
        return total_hombres, total_mujeres

    def __str__(self):
        return f"Nombre: {self.nombre:<10} Rango: {self.rango:<16} Costo: ${self.costo:,.2f}"

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = list()

    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)

    def total_general(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.subtotal()
        return total

    def __str__(self):
        return f"\nNombre: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}"

def main():
    os.system("cls")
    print("REPORTE DEL CLUB DEPORTIVO")
    club = Academia(nombre="Academia Santos Laguna", propietario="Francisco Nava", domicilio="Aguanaval 123, Hidráulica")
    
    # categorías
    club.agregarCategoria(Categoria(nombre="Junior A", rango="2006/2007/2008", costo=1250))
    club.agregarCategoria(Categoria(nombre="Junior B", rango="2009/2010/2011", costo=850))
    club.agregarCategoria(Categoria(nombre="Pony A", rango="2012/2013/2014", costo=700))
    
    # jugadores
    # junior a
    club.categorias[0].agregarJugador(Jugador(nombre="Alexander López", añonac=2006, sexo="H", becado=0))
    club.categorias[0].agregarJugador(Jugador(nombre="Uriel Puga", añonac=2007, sexo="H", becado=1))
    club.categorias[0].agregarJugador(Jugador(nombre="Alejandra Escalona", añonac=2008, sexo="M", becado=0))
    # junior b
    club.categorias[1].agregarJugador(Jugador(nombre="Armando Santana", añonac=2009, sexo="H", becado=0))
    club.categorias[1].agregarJugador(Jugador(nombre="Daniel Mijares", añonac=2010, sexo="H", becado=0))
    club.categorias[1].agregarJugador(Jugador(nombre="Antonio Hernández", añonac=2011, sexo="M", becado=1))
    # pony a
    club.categorias[2].agregarJugador(Jugador(nombre="Andrea Solis", añonac=2012, sexo="M", becado=1))
    club.categorias[2].agregarJugador(Jugador(nombre="Marissa Hernández", añonac=2013, sexo="M", becado=1))
    club.categorias[2].agregarJugador(Jugador(nombre="Diana Soto", añonac=2014, sexo="M", becado=0))
    
    # reporte
    print(f"{club}")

    total_general = 0
    total_hombres = 0
    total_mujeres = 0
    
    print("\n>> Datos generales de las Categorías\n")
    for categoria in club.categorias:
        print(categoria)
        total_general += categoria.subtotal()
        for jugador in categoria.jugadores:
            if jugador.sexo == 'H':
                total_hombres += 1
            elif jugador.sexo == 'M':
                total_mujeres += 1
    
    print("\n>> Jugadores por Categoría")
    for categoria in club.categorias:
        print(f"\n> {categoria.nombre} - {categoria.rango} - {len(categoria.jugadores)} - Subtotal: ${categoria.subtotal():,.2f}\n")
        for jugador in categoria.jugadores:
            print(f"{jugador}")
    
    print(f"\nTotal de Categorías: {len(club.categorias)}")
    print(f"Total de Hombres: {total_hombres}")
    print(f"Total de Mujeres: {total_mujeres}")
    print(f"\nTotal General: ${total_general:,.2f}")

if __name__ == "__main__":
    main()