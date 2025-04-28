from django import forms
from employees.models import Employee

# Each line has its own scenarios; each scenario starts with two placeholder tasks that you can customize
SCENARIO_CONFIG = {
    'line1': {
        'pc_production': [
            # Process
            ('Process', 'Slicing'),
            ('Process', 'Seasoning'),
            ('Process', 'Slicing & Seasoning BR'),
            ('Process', 'Fryer Tech'),
            ('Process', 'Fryer Tech'),
            # Primary
            ('Primary Packaging', 'Zone 1'),
            ('Primary Packaging', 'Zone 2'),
            ('Primary Packaging', 'Zone 1 & 2 BR'),
            ('Primary Packaging', 'Zone 3'),
            ('Primary Packaging', 'Zone 4'),
            ('Primary Packaging', 'Zone 3 & 4 BR'),
            ('Primary Packaging', 'Inserter Operator'),
            ('Primary Packaging', 'EOL Operator'),
            ('Primary Packaging', 'EOL Support'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            # Multipack
            ('Multipack Packaging', 'F80'),
            ('Multipack Packaging', 'F82'),
            ('Multipack Packaging', 'F83'),
            ('Multipack Packaging', 'F84'),
            ('Multipack Packaging', 'F85'),
            ('Multipack Packaging', 'F86'),
            ('Multipack Packaging', 'F87'),
            ('Multipack Packaging', 'F88'),
            ('Multipack Packaging', 'F89'),
            ('Multipack Packaging', 'F90'),
            ('Multipack Packaging', 'F100'),
            ('Multipack Packaging', 'F100 Packer'),
            ('Multipack Packaging', 'F100 Packer'),
            ('Multipack Packaging', 'F100 Packer BR'),
            ('Multipack Packaging', 'L1 MP BR'),
            ('Multipack Packaging', 'L1 MP BR'),
            ('Multipack Packaging', 'L1 MP BR'),
            ('Multipack Packaging', 'Spiral'),
            ('Multipack Packaging', 'WIP'),
            ('Multipack Packaging', 'Spiral & WIP BR'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            # Palletiser
            ('Palletiser', 'Palletiser Operator'),
            ('Palletiser', 'Palletiser Tech'),
            # Despatch
            ('Despatch', 'Line Supply'),
        ],
        'engineering': [
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Palletiser'),
            ('Debris Removal', 'Seasoning'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
        ],
        'boilout': [
            # Process tasks
            ('Process', 'Fryer'),
            ('Process', 'Fryer'),
            # Seasoning (5 people)
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            # Allergen Champ (twice)
            ('Process', 'Allergen Champ'),
            ('Process', 'Allergen Champ'),
            # Primary Packaging – Stages (7 people)
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            # Ishidas
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            # Dishwasher (2 people)
            ('Primary Packaging', 'Dishwasher'),
            ('Primary Packaging', 'Dishwasher'),
            # TNAs (4 people)
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            # PWRs (5 person)
            ('Multipack Packaging', 'PWRs'),
            ('Multipack Packaging', 'PWRs'),
            ('Multipack Packaging', 'Schuberts'),
            ('Multipack Packaging', 'Schuberts'),
            ('Multipack Packaging', 'Schuberts'),
            # Palletiser Robots (1 person)
            ('Palletiser', 'Robots'),
        ],
    },
    
    'line2': {
        'pc_production': [
            ('Process', 'Slicing'),
            ('Process', 'Seasoning'),
            ('Process', 'Slicing & Seasoning BR'),
            ('Process', 'Fryer Tech'),
            ('Process', 'Fryer Tech'),
            ('Primary Packaging', 'Zone 1'),
            ('Primary Packaging', 'Zone 2'),
            ('Primary Packaging', 'Zone 3'),
            ('Primary Packaging', 'Zone 1, 2 & 3 BR'),
            ('Primary Packaging', 'Zone 4'),
            ('Primary Packaging', 'Zone 5'),
            ('Primary Packaging', 'Zone 6'),
            ('Primary Packaging', 'Zone 4, 5 & 6 BR'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Multipack Packaging', 'G91'),
            ('Multipack Packaging', 'G91 EOL Packer'),
            ('Multipack Packaging', 'G97'),
            ('Multipack Packaging', 'G97 EOL Packer'),
            ('Multipack Packaging', 'EOL Packer BR'),
            ('Multipack Packaging', 'G98'),
            ('Multipack Packaging', 'G99'),
            ('Multipack Packaging', 'G50'),
            ('Multipack Packaging', 'MP BR'),
            ('Multipack Packaging', 'G53 Operator'),
            ('Multipack Packaging', 'G53 Operator'),
            ('Multipack Packaging', 'G53 Econopac'),
            ('Multipack Packaging', 'G53 Palletiser'),
            ('Multipack Packaging', 'G53 Palletiser'),
            ('Multipack Packaging', 'G54 Operator'),
            ('Multipack Packaging', 'G54 Operator'),
            ('Multipack Packaging', 'G54 Econopac'),
            ('Multipack Packaging', 'G54 Rework'),
            ('Multipack Packaging', 'WIP'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'MP Tech'),
            ('Multipack Packaging', 'Line Balancer'),
            # Palletiser tasks
            ('Palletiser', 'Palletiser Operator'),
            ('Palletiser', 'Palletiser Tech'),
            # Despatch task
            ('Despatch', 'Line Supply'),
        ],
        'engineering': [
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Palletiser'),
            ('Debris Removal', 'Seasoning'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Multipack Area'),
        ],
        'boilout': [
            # Process tasks
            ('Process', 'Fryer'),
            ('Process', 'Fryer'),
            # Seasoning (7 people)
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            # Allergen Champ (twice)
            ('Process', 'Allergen Champ'),
            ('Process', 'Allergen Champ'),
            # Primary Packaging – Stages (5 people)
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            # Ishidas
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            # Dishwasher (2 people)
            ('Primary Packaging', 'Dishwasher'),
            ('Primary Packaging', 'Dishwasher'),
            # TNAs (5 people)
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            # DTC (4 people)
            ('Multipack Packaging', 'DTC'),
            ('Multipack Packaging', 'DTC'),
            ('Multipack Packaging', 'DTC'),
            ('Multipack Packaging', 'DTC'),
            # LMPs (1 people)
            ('Multipack Packaging', 'LMPs'),
            # PWRs (1 person)
            ('Multipack Packaging', 'PWRs'),
            # Palletiser Auto P (1 person)
            ('Palletiser', 'Auto P'),
        ],
    },
    'line3': {
        'pc_production': [
            # Process
            ('Process', 'Slicing'),
            ('Process', 'Seasoning'),
            ('Process', 'Slicing & Seasoning BR'),
            ('Process', 'Fryer Tech'),
            ('Process', 'Fryer Tech'),
            # Packaging
            ('Primary Packaging', 'Zone 1'),
            ('Primary Packaging', 'Zone 2'),
            ('Primary Packaging', 'Zone 1 & 2 BR'),
            ('Primary Packaging', 'Zone 3'),
            ('Primary Packaging', 'Zone 4'),
            ('Primary Packaging', 'Zone 3 & 4 BR'),
            ('Primary Packaging', 'Zone 5'),
            ('Primary Packaging', 'Zone 6'),
            ('Primary Packaging', 'Zone 5 & 6 BR'),
            ('Primary Packaging', 'Zone 7'),
            ('Primary Packaging', 'Zone 8'),
            ('Primary Packaging', 'Zone 7 & 8'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            # Auto P
            ('Palletiser', 'Auto P Tech'),
            ('Palletiser', 'Auto P Operator'),
            ('Palletiser', 'Auto P Checkweigher'),
            ('Palletiser', 'Auto P Checkweigher'),
            ('Palletiser', 'Auto P Checkweigher'),
            ('Palletiser', 'Auto P Overflow'),
            ('Palletiser', 'Auto P Overflow'),
            # Despatch
            ('Despatch', 'Line Supply'),
        ],
        'sensations_production': [
            # Process
            ('Process', 'Slicing'),
            ('Process', 'Seasoning'),
            ('Process', 'Slicing & Seasoning BR'),
            ('Process', 'Fryer Tech'),
            ('Process', 'Fryer Tech'),
            # Packaging
            ('Primary Packaging', 'Zone 1'),
            ('Primary Packaging', 'Zone 2'),
            ('Primary Packaging', 'Zone 1 & 2 BR'),
            ('Primary Packaging', 'Zone 3'),
            ('Primary Packaging', 'Zone 4'),
            ('Primary Packaging', 'Zone 3 & 4 BR'),
            ('Primary Packaging', 'Zone 5'),
            ('Primary Packaging', 'Zone 6'),
            ('Primary Packaging', 'Zone 5 & 6 BR'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            ('Primary Packaging', 'Packaging Tech'),
            # Multipack
            ('Multipack Packaging', 'H71 Operator'),
            ('Multipack Packaging', 'H71 BR'),
            ('Multipack Packaging', 'H71 Stockloader'),
            ('Multipack Packaging', 'H71 Stockloader'),
            # Auto P
            ('Palletiser', 'Auto P Tech'),
            ('Palletiser', 'Auto P Operator'),
            ('Palletiser', 'Auto P Checkweigher'),
            ('Palletiser', 'Auto P Overflow'),
            ('Palletiser', 'Auto P Overflow'),
            # Despatch
            ('Despatch', 'Line Supply'),
        ],
        'engineering': [
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Primary Packaging'),
            ('Engineering', 'Multipack Packaging'),
            ('Engineering', 'Palletiser'),
            ('Debris Removal', 'Seasoning'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Multipack Area'),
        ],
        'boilout': [
            # Process tasks
            ('Process', 'Fryer'),
            ('Process', 'Fryer'),
            # Seasoning (4 people)
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            ('Process', 'Seasoning'),
            # Allergen Champ (twice)
            ('Process', 'Allergen Champ'),
            ('Process', 'Allergen Champ'),
            # Primary Packaging – Stages (5 people)
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            # Ishidas
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            # Dishwasher (2 people)
            ('Primary Packaging', 'Dishwasher'),
            ('Primary Packaging', 'Dishwasher'),
            # TNAs (5 people)
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            ('Primary Packaging', 'TNAs'),
            # PWRs (1 person)
            ('Multipack Packaging', 'PWRs'),
            # Palletiser Auto P (1 person)
            ('Palletiser', 'Auto P'),
        ],
    },
    'line4': {
        'snacks_production': [
            # Process
            ('Process', 'Extrution Tech'),
            ('Process', 'Extuder A Op'),
            ('Process', 'Extruder B Op'),
            ('Process', 'Seasoning'),
            # Primary Packaging
            ('Primary Packaging', 'Zone 1'),
            ('Primary Packaging', 'Zone 2'),
            ('Primary Packaging', 'Zone 3'),
            ('Primary Packaging', 'Zone 1, 2 & 3 BR'),
            ('Primary Packaging', 'Packaging Tech'),
            # Placeholder for handpacker block
            ('Handpackers', 'HANDPACKERS'),
            # Multipack Packaging
            ('Multipack Packaging', 'PWR 3 - 8'),
            ('Multipack Packaging', 'PWR 9 - 14'),
            ('Multipack Packaging', 'PWR Support'),
            ('Multipack Packaging', 'PWR BR'),
            ('Multipack Packaging', 'BPA 3'),
            ('Multipack Packaging', 'BPA 4'),
            ('Multipack Packaging', 'BPA BR'),
            ('Multipack Packaging', 'MP Tech'),
            # Palletiser
            ('Palletiser', 'Palletiser Tech'),
            ('Palletiser', 'Palletiser Op'),
            ('Palletiser', 'Palletiser Op'),
            # Despatch
            ('Despatch', 'Line Supply'),
        ],
        'engineering': [
            # Engineering
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Engineering', 'Process'),
            ('Primary Packaging', 'Primary Packaging'),
            ('Primary Packaging', 'Primary Packaging'),
            ('Primary Packaging', 'Primary Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Multipack Packaging', 'Multipack Packaging'),
            ('Palletiser', 'Palletiser'),
            # Debris Removal
            ('Debris Removal', 'Seasoning'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Stages'),
            ('Debris Removal', 'Ishidas'),
            ('Debris Removal', 'Ishidas'),
            ('Multipack Area', 'Multipack Area'),
            ('Multipack Area', 'Multipack Area'),
        ],
        'boilout': [
            # Process
            ('Process', 'Extrusion'),
            ('Process', 'Oven'),
            ('Process', 'Oven'),
            ('Process', 'Seasoning'),
            ('Process', 'Allergen Champ'),
            # Primary Packaging
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Stages'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Ishidas'),
            ('Primary Packaging', 'Dishwasher'),
            ('Primary Packaging', 'TNAs'),
            # Multipack Packaging
            ('Multipack Packaging', 'PWRs'),
            # Palletiser
            ('Palletiser', 'Auto P'),
        ],
    },
}

class ShiftAssignmentForm(forms.Form):
    """
    Dynamically generates one ChoiceField per task in the chosen line/scenario.

    :param shift: Shift instance, to filter employee pool by home team
    :param line: key in SCENARIO_CONFIG ('line1'..'line4')
    :param scenario: key in SCENARIO_CONFIG[line] ('pc_production', 'engineering', 'boilout')
    """
    def __init__(self, *args, shift=None, line='line1', scenario='pc_production', **kwargs):
        super().__init__(*args, **kwargs)
        if not shift:
            raise ValueError("ShiftAssignmentForm requires a shift instance")
        self.shift = shift
        # Ensure valid line and scenario
        self.line = line if line in SCENARIO_CONFIG else 'line1'
        line_scenarios = SCENARIO_CONFIG[self.line]
        self.scenario = scenario if scenario in line_scenarios else next(iter(line_scenarios))

        # Pool of employees whose home shift matches this team
        pool = Employee.objects.filter(active=True, shift=shift.team)

        # Dynamically create one field per (area, role) in the chosen scenario
        tasks = line_scenarios[self.scenario]
        for idx, (area, role) in enumerate(tasks):
            field_name = f"assign_{idx}"
            choices = [('', '— none —')] + [
                (e.pk, e.full_name)
                for e in pool
                if e.area.name == area and e.role == role
            ]
            self.fields[field_name] = forms.ChoiceField(
                choices=choices,
                required=False,
                label=f"{area} – {role}",
                widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
            )

    def get_task_fields(self):
        """
        Returns list of (field_name, label) for template rendering in order.
        """
        return [(name, field.label) for name, field in self.fields.items()]
