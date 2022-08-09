from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
import conversoes


class Conversor(GridLayout):

    per_volume_units = ['mg/L', 'µg/L', 'ng/L', 'g/L', 'mol/L', 'µg/mL', 'mg/mL']
    per_mass_units = ['mg/Kg', 'µg/Kg']
    molar_units = ['mol/L']
    units_list = ['mg/L', 'µg/L', 'ng/L', 'g/L', 'mol/L', 'µg/mL', 'mg/Kg', 'mg/mL', 'µg/Kg']
    input_unit = ""
    output_unit = ""

    def input_spinner_clicked(self, value):
        self.ids.input_molar_mass.disabled = True
        self.ids.input_density.disabled = True
        values_list = self.units_list.copy()
        self.input_unit = value
        if self.input_unit in self.molar_units:
            self.ids.input_molar_mass.disabled = False
        if self.input_unit in self.per_mass_units:
            self.ids.input_density.disabled = False
        values_list.remove(value)
        self.ids.output_dropdown.values = values_list

    def output_spinner_clicked(self, value):
        self.ids.input_molar_mass.disabled = True
        self.ids.input_density.disabled = True
        self.output_unit = value
        if self.output_unit in self.molar_units:
            self.ids.input_molar_mass.disabled = False
        if self.output_unit in self.per_mass_units and self.input_unit not in self.per_mass_units:
            self.ids.input_density.disabled = False

    def on_click_converter(self, input_value, density="1", molar_mass="1"):
        if input_value == '':
            self.ids.resultado_label.text = 'Nenhum valor foi digitado'
        else:
            if self.input_unit == "mg/L":
                if self.output_unit == "µg/L":
                    result = conversoes.mgL_to_mcgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mgL_to_ngL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mgL_to_gL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.mgL_to_mcgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.mgL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.mgL_to_mgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mgL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.mgL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "µg/L":
                if self.output_unit == "mg/L":
                    result = conversoes.mcgL_to_mgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mcgL_to_ngL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mcgL_to_gL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mcgL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.mcgL_to_mcgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.mcgL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.mcgL_to_mgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.mcgL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "ng/L":
                if self.output_unit == "µg/Kg":
                    result = conversoes.ngL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.ngL_to_mcgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.ngL_to_mcgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/L":
                    result = conversoes.ngL_to_mgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.ngL_to_mgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.ngL_to_gL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.ngL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.ngL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "g/L":
                if self.output_unit == "mg/L":
                    result = conversoes.gL_to_mgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.gL_to_mcgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.gL_to_ngL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.gL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.gL_to_mcgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.gL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.gL_to_mgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.gL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "mol/L":
                if self.output_unit == "mg/L":
                    result = conversoes.molL_to_mgL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.molL_to_mcgL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.molL_to_ngL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.molL_to_gL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.molL_to_mcgmL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.molL_to_mgKg(float(input_value), float(density), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.molL_to_mgmL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.molL_to_mcgKg(float(input_value), float(density), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "µg/mL":
                if self.output_unit == "mg/L":
                    result = conversoes.mcgmL_to_mgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.mcgmL_to_mcgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mcgmL_to_ngL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mcgmL_to_gL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mcgmL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.mcgmL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.mcgmL_to_mgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.mcgmL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "mg/Kg":
                if self.output_unit == "mg/L":
                    result = conversoes.mgKg_to_mgL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.mgKg_to_mcgL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mgKg_to_ngL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mgKg_to_gL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mgKg_to_molL(float(input_value), float(density), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.mgKg_to_mcgmL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.mgKg_to_mgmL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.mgKg_to_mcgKg(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "mg/mL":
                if self.output_unit == "mg/L":
                    result = conversoes.mgmL_to_mgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.mgmL_to_mcgL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mgmL_to_ngL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mgmL_to_gL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mgmL_to_molL(float(input_value), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.mgmL_to_mcgmL(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.mgmL_to_mgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/Kg":
                    result = conversoes.mgmL_to_mcgKg(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
            if self.input_unit == "µg/Kg":
                if self.output_unit == "mg/L":
                    result = conversoes.mcgKg_to_mgL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/L":
                    result = conversoes.mcgKg_to_mcgL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "ng/L":
                    result = conversoes.mcgKg_to_ngL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "g/L":
                    result = conversoes.mcgKg_to_gL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mol/L":
                    result = conversoes.mcgKg_to_molL(float(input_value), float(density), float(molar_mass))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "µg/mL":
                    result = conversoes.mcgKg_to_mcgmL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/Kg":
                    result = conversoes.mcgKg_to_mgKg(float(input_value))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"
                if self.output_unit == "mg/mL":
                    result = conversoes.mcgKg_to_mgmL(float(input_value), float(density))
                    self.ids.resultado_label.text = f"{input_value} {self.input_unit} corresponde a {str(result)}" \
                                                    f" {self.output_unit}"


class ConversorApp(MDApp):
    def build(self):
        return Conversor()


if __name__ == '__main__':
    ConversorApp().run()
