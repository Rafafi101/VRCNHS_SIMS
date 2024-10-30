from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Gradelevel, Classroom


@receiver(post_migrate)
def populate_gradelevels_and_classrooms(sender, **kwargs):
    if sender.name == 'classrooms':
        gradelevels = [
            'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'
        ]
        classrooms = {
            'Grade 7': ['Stargazer', 'Aster', 'Sampaguita', 'Everlasting', 'Dama De Noche', 'Tulip', 'Yellowbell', 'Daffodil', 'Daisy', 'Carnation', 'Poinsettia', 'Iris', 'Rose', 'Rafflesia', 'Lily', 'Hibiscus', 'Lavender', 'Lilac', 'Buttercup', 'Cherry Blossom', 'Magnolia', 'Marigold', 'SECTIONING'],
            'Grade 8': ['DIAMOND', 'ZIRCON', 'JADE', 'GARNET', 'SELENITE', 'AMBER', 'CITRINE', 'MAGNETITE', 'FLOURITE', 'SPINEL', 'TANZANITE', 'KYANITE', 'AQUAMARINE', 'PEARL', 'RUBY', 'ONYX', 'TURQUOISE', 'TOPAZ', 'ZOISITE', 'VERDITE', 'BERYL', 'CAVANSITE', 'CRYSTAL', 'AMMOLITE', 'MOONSTONE', 'STARLITE', 'SECTIONING'],
            'Grade 9': ['Platinum', 'Silver', 'Nickel', 'Zinc', 'Sodium', 'Manganese', 'Magnesium', 'Lithium', 'Vanadium', 'Francium', 'Gallium', 'Copper', 'Strontium', 'Potassium', 'Thallium', 'Uranium', 'Gold', 'Cobalt', 'Mercury', 'Titanium', 'Calcium', 'Iron', 'Cesium', 'Krypton', 'Scandium', 'Barium', 'Polonium', 'Lead', 'Zirconium', 'Palladium', 'Radium', 'Osmium', 'SECTIONING'],
            'Grade 10': ['ST. JOHN', 'ST. MATTHEW', 'ST. AUGUSTINE', 'ST. JAMES', 'ST. ANDREW', 'ST. LAWRENCE', 'ST. JUDE', 'ST. MATTHIAS', 'ST. PIUS', 'ST. CLEMENT', 'ST. VICTOR', 'ST. JOACHIM', 'ST. VALENTINE', 'ST. STEPHEN', 'ST. LUKE', 'ST. VINCENT', 'ST. PAUL', 'ST. JOSEPH', 'ST. FRANCIS', 'ST. ISIDORE', 'ST. THOMAS', 'ST. BENEDICT', 'ST. DOMINIC', 'ST. SIMON', 'ST. XAVIER', 'ST. PHILIP', 'ST. SEBASTIAN', 'ST. ANTHONY', 'ST. AMBROSE', 'ST. NICHOLAS', 'ST. IGNATIUS', 'ST. MICHAEL', 'SECTIONING'],
            'Grade 11': ['EINSTEIN', 'MORGAN', 'LOCKE', 'MARX', 'MASLOW', 'COOPER', 'FRANKLIN', 'RAMSAY', 'SECTIONING'],
            'Grade 12': ['ZUCKERBERG', 'RICHARDS', 'MAXWELL', 'DALTON', 'KEYNES', 'AGUINALDO', 'QUEZON', 'Lithium', 'SOCRATES', 'PLATO', 'FOR DEPARTURE', 'SECTIONING'],
        }

        for gradelevel in gradelevels:
            # Create or get gradelevel
            grade_obj, _ = Gradelevel.objects.get_or_create(
                gradelevel=gradelevel)

            # Create classrooms for the gradelevel
            for classroom in classrooms[gradelevel]:
                Classroom.objects.get_or_create(
                    gradelevel=grade_obj, classroom=classroom)
