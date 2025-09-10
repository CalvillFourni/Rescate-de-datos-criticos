class Tarea:
    def __init__(self, nombre, descripcion, duracion, dependencias=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion  # en minutos
        self.dependencias = dependencias if dependencias else []
        self.completada = False

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} ({self.duracion} min)"

class RescateDatosCriticos:
    def __init__(self):
        self.tareas = self._crear_tareas()
        self.tecnicos_disponibles = 3
        self.tiempo_total = 120  # minutos

    def _crear_tareas(self):
        # Definición de tareas y dependencias
        tareas = {
            "A": Tarea("A", "Identificar servidores afectados", 15),
            "B": Tarea("B", "Priorizar datos críticos", 20, ["A"]),
            "C": Tarea("C", "Activar protocolo de recuperación", 10, ["A"]),
            "D": Tarea("D", "Asignar técnicos a servidores", 5, ["B", "C"]),
            "E": Tarea("E", "Recuperar datos de servidor 1", 30, ["D"]),
            "F": Tarea("F", "Recuperar datos de servidor 2", 25, ["D", "E"]),
            "G": Tarea("G", "Validar integridad de datos recuperados", 15, ["F"]),
            "H": Tarea("H", "Generar informe preliminar para dirección", 10, ["G"]),
            "I": Tarea("I", "Comunicar a clientes afectados", 20, ["G"]),
            "J": Tarea("J", "Coordinar con equipo legal", 15, ["G"]),
            "K": Tarea("K", "Preparar plan de contingencia", 25, ["G"]),
        }
        return tareas

    def definir_objetivo(self):
        return ("Rescatar los datos médicos más críticos en 120 minutos, "
                "optimizando recursos y asegurando comunicación efectiva.")

    def diagrama_flujo(self):
        print("Diagrama de flujo de tareas y dependencias:")
        for t in self.tareas.values():
            deps = ", ".join(t.dependencias) if t.dependencias else "Ninguna"
            print(f"{t.nombre} -> Depende de: {deps}")

    def nivelar_recursos(self):
        print(f"Técnicos disponibles: {self.tecnicos_disponibles}")
        print("Solo se puede recuperar datos de un servidor a la vez.")
        print("Asignación óptima de técnicos en tareas críticas.")

    def plan_comunicacion(self):
        print("Comunicación de crisis:")
        print("- Informe preliminar a dirección tras validación de datos (H)")
        print("- Comunicación a clientes afectados (I)")
        print("- Coordinación con equipo legal (J)")
        print("- Preparación de plan de contingencia (K)")

    def resumen_tareas(self):
        print("Resumen de tareas, descripciones y duraciones:")
        for t in self.tareas.values():
            print(str(t))

if __name__ == "__main__":
    rescate = RescateDatosCriticos()
    print("Objetivo del Proyecto:")
    print(rescate.definir_objetivo())
    print("\n---")
    rescate.diagrama_flujo()
    print("\n---")
    rescate.nivelar_recursos()
    print("\n---")
    rescate.plan_comunicacion()
    print("\n---")
    rescate.resumen_tareas()