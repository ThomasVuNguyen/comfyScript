main() {
  Animal dog = Animal("thomas", 4, 100);
  dog.display();
}

class Animal {
  String? name;
  int? numberOfLegs;
  int? lifeSpan;
  Animal(String name, int numberOfLegs, int lifeSpan) {
    this.name = name;
    this.numberOfLegs = numberOfLegs;
    this.lifeSpan = lifeSpan;
  }
  void display() {
    print("$name has $numberOfLegs and can live up to $lifeSpan");
  }
}
