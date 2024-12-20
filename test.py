import json
from ant_class import Ant


# Beispielklasse für die Objekte
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {"name": self.name, "value": self.value}


# Listen mit Objekten
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [Ant(50, 50, 50,50 , 0)]  # Liste mit Objekten


# Funktion, um komplexe Objekte (z.B. aus `list3`) zu serialisieren
def serialize_object(obj):
    if hasattr(obj, "to_dict"):  # Wenn das Objekt eine to_dict-Methode hat
        return obj.to_dict()
    else:
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


# Funktion, um die Listen in eine Datei zu speichern
def save_step(filename, step, data):
    with open(filename, 'a') as file:  # 'a' für Anhängen an die Datei
        file.write(f"Step {step}:\n")
        json.dump(data, file, indent=4, default=serialize_object)  # Default für Objekte
        file.write("\n\n")  # Leerzeilen für bessere Lesbarkeit


# Datei, in der die Schritte gespeichert werden
filename = "ant_movment.json"

# Schritt 1: Ersten Zustand speichern
step = 1
save_step(filename, step, {"list1": list1, "list2": list2, "list3": list3})

# Schritt 2: Listen verändern
list1.append(4)
list2.append('d')
list3.append(Item("Item4", 40))
step += 1
save_step(filename, step, {"list1": list1, "list2": list2, "list3": list3})

# Schritt 3: Weitere Modifikationen
list1.remove(2)
list2.pop(0)
list3[0].value = 15  # Wert eines Objekts ändern
step += 1
save_step(filename, step, {"list1": list1, "list2": list2, "list3": list3})

print(f"Alle Schritte wurden in {filename} gespeichert.")