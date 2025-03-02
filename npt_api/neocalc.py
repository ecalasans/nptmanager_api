import json


class HV:
    def __init__(self, peso, volume, vig):
        self.peso = peso
        self.volume = volume
        self.vig = vig
        self.na20 = 3.4
        self.ca10 = 9.0
        self.na = None
        self.ca = None
        self.k = None
        self.mg = None
        self.cK = None
        self.cMg = None

    def get_peso(self):
        return self.peso

    def get_vig(self):
        return self.vig

    def get_volume(self):
        return self.volume

    def set_na(self, dose):
        self.na = dose

    def get_na(self):
        return self.na

    def set_ca(self, dose):
        self.ca = dose

    def get_ca(self):
        return self.ca

    def set_k(self, dose):
        self.k = dose

    def get_k(self):
        return self.k

    def set_mg(self, dose):
        self.mg = dose

    def get_mg(self):
        return self.mg

    def set_cK(self, sel_k):
        if sel_k == 0:
            self.cK = 1.34  # KCl 10%
        else:
            self.cK = 2.56  # KCl 19.1% or default

    def set_cMg(self, sel_mg):
        if sel_mg == 0:
            self.cMg = 0.8  # MgSO4 10%
        else:
            self.cMg = 4.0  # MgSO4 50% or default

    # Cálculo do volume de eletrólitos
    def vol_na(self):
        return self.peso * self.na / self.na20

    def vol_ca(self):
        return self.peso * self.ca

    def vol_k(self):
        return self.peso * self.k / self.cK

    def vol_mg(self):
        return self.peso * self.mg / self.cMg

    # Volume de cálculo
    def volume_calculo(self):
        return self.peso * self.volume

    # Concentração Teórica
    def concentracao_teorica(self):
        gr_glicose = 1.44 * self.peso * self.vig
        return (100 * gr_glicose) / self.volume_calculo()

    # Concentração Real
    def concentracao_real(self, sol_glic):
        conc_real = 0
        if sol_glic == 0:  # Glicose 5%
            conc_real = (self.volume_glic_5() * 0.05 + self.volume_glic_50() * 0.5) / self.volume_total()
        elif sol_glic == 1:  # Glicose 10%
            conc_real = self.volume_glic_10() * 0.1 / self.volume_total()
        else:
            conc_real = (self.volume_glic_5() * 0.05 + self.volume_glic_50() * 0.5) / self.volume_total()
        return conc_real

    # Volume de glicose a 50%
    def volume_glic_50(self):
        resultado = 0.0
        if self.concentracao_teorica() > 5.0:
            resultado = (self.volume_calculo() * (self.concentracao_teorica() - 5.0)) / 45
        return resultado

    # Volume de glicose a 10%
    def volume_glic_10(self):
        return (self.peso * self.vig * 1.44) * 10

    # Volume de glicose a 5%
    def volume_glic_5(self):
        resultado = 0.0
        if self.concentracao_teorica() > 5.0:
            resultado = self.volume_calculo() - self.volume_glic_50()
        return resultado

    def volume_ABD(self):
        resultado = 0.0
        if self.concentracao_teorica() < 5.0:
            resultado = self.volume_calculo() - (self.volume_glic_50() + self.vol_na() + self.vol_ca()
                                                 + self.vol_k() + self.vol_mg())
        return resultado

    def volume_total(self, sel_glic):
        vt = 0
        if sel_glic == 0:  # Glicose 50 + SG 5%
            vt = self.volume_glic_5() + self.volume_glic_50() + self.volume_ABD() + \
                 self.vol_na() + self.vol_k() + self.vol_ca() + self.vol_mg()
        elif sel_glic == 1:  # Glicose 10%
            vt = self.volume_glic_10() + self.volume_ABD() + \
                 self.vol_na() + self.vol_k() + self.vol_ca() + self.vol_mg()
        else:
            vt = self.volume_glic_5() + self.volume_glic_50() + self.volume_ABD() + \
                 self.vol_na() + self.vol_k() + self.vol_ca() + self.vol_mg()
        return vt

    def to_json(self):
        import json
        arq = {
            'peso': self.peso,
            'volume': self.volume,
            'vig': self.vig,
            'concentracaoTeorica': round(self.concentracao_teorica(), 1),
            'concentracaoReal': round(self.concentracao_real(0), 1),
            'vGlic5': round(self.volume_glic_5(), 1),
            'vGlic10': round(self.volume_glic_10(), 1),
            'vGlic50': round(self.volume_glic_50(), 1),
            'vABD': round(self.volume_ABD(), 1),
            'vCa': round(self.vol_ca(), 1),
            'vNa': round(self.vol_na(), 1),
            'vK': round(self.vol_k(), 1),
            'vMg': round(self.vol_mg(), 1),
            'volTotal': round(self.volume_total(0), 1)
        }
        return json.dumps(arq)


class NPT(HV):
    def __init__(self, peso, volume, vig, aac, lip):
        super().__init__(peso, volume, vig)
        self.aac = aac
        self.lip = lip
        self.fc = (self.volume_calculo() + 20) / self.volume_calculo()
        self.p = None
        self.optVit = None
        self.opOligo = None

    # Setters and getters
    # Amino acids
    def get_aac(self):
        return self.aac

    def set_aac(self, dose_aac):
        self.aac = dose_aac

    # Lipids
    def get_lip(self):
        return self.lip

    def set_lip(self, dose_lip):
        self.lip = dose_lip

    # Phosphorus
    def set_p(self, dose_p):
        self.p = dose_p

    def get_p(self):
        return self.p

    # Vitamins
    def set_opt_vit(self, opcao):
        self.optVit = opcao

    def get_opt_vit(self):
        return self.optVit

    # Oligoelements
    def set_op_oligo(self, opcao):
        self.opOligo = opcao

    def get_op_oligo(self):
        return self.opOligo

    # Correction factor
    def get_fc(self):
        return self.fc

    def set_fc(self, volume_equipo):
        self.fc = (self.volume_calculo() + volume_equipo) / self.volume_calculo()

    # Overridden methods with correction factor
    def vol_na(self):
        if self.p != 0 and self.na and self.na >= 2:
            return super().vol_na() * self.fc
        return 0

    def vol_ca(self):
        return super().vol_ca() * self.fc

    def vol_mg(self):
        return super().vol_mg() * self.fc

    def vol_k(self):
        return super().vol_k() * self.fc

    def vol_p(self):
        return self.peso * self.p * self.fc if self.p else 0

    # Nutrients
    def vol_aac(self):
        return self.peso * self.aac * 10 * self.fc

    def vol_lip(self):
        return self.peso * self.lip * 5 * self.fc

    def vol_glic(self):
        return self.peso * self.vig * 2 * 1.44 * self.fc

    def vol_vit(self):
        vitaminas = [0, 0]

        if self.optVit == 1:  # Frutovitam
            vitaminas[0] = self.peso * 2.0 * self.fc
        elif self.optVit == 2:  # Trezevit A/B
            if self.peso >= 3.0:
                vitaminas[0] = 5 * self.peso * self.fc
                vitaminas[1] = 5 * self.peso * self.fc
            elif 1.0 < self.peso < 3.0:
                vitaminas[0] = 3.25 * self.peso * self.fc
                vitaminas[1] = 3.25 * self.peso * self.fc
            else:
                vitaminas[0] = 1.5 * self.peso * self.fc
                vitaminas[1] = 1.5 * self.peso * self.fc
        elif self.optVit == 3:  # Polivit A/B
            if self.peso <= 10.0:
                vitaminas[0] = self.peso * 4.0 * self.fc
                vitaminas[1] = self.peso * 2.0 * self.fc
            else:
                vitaminas[0] = 10.0
                vitaminas[1] = 5.0
        else:
            vitaminas[0] = 5 * self.peso * self.fc
            vitaminas[1] = 5 * self.peso * self.fc

        return vitaminas

    def v_total_vit(self, vitaminas):
        return vitaminas[0] + vitaminas[1]

    def vol_oligo(self):
        resultado = 0.0

        if self.opOligo == 1:  # Ped-Element
            resultado = self.peso * 0.2 * self.fc
        elif self.opOligo == 2:  # Oliped
            resultado = self.peso * self.fc
        elif self.opOligo == 3:  # Ad-Element
            resultado = self.peso * 0.05 * self.fc
        elif self.opOligo == 4:  # Politrace 4
            resultado = self.peso * 0.1 * self.fc
        elif self.opOligo == 5:  # Tracitrans Plus
            resultado = self.peso * 0.3 * self.fc

        return resultado

    # NPT controls
    def kcal_glic(self):
        return 3.4 * self.peso * self.vig * 1.44

    def kcal_lip(self):
        return 9 * self.peso * self.lip

    def kcal_aac(self):
        return 4 * self.peso * self.aac

    def kcal_nao_proteicas(self):
        return self.kcal_glic() + self.kcal_lip()

    def oferta_calorica_total(self):
        return self.kcal_lip() + self.kcal_glic() + self.kcal_aac()

    def total_cations(self):
        return (self.vol_ca() * 0.45 + self.vol_mg() * 4) * 1000 / self.volume_total_npt()

    def total_n(self):
        return self.peso * self.aac / 6.25

    def total_ca(self):
        return (self.vol_ca() * 450) / self.volume_total_npt()

    def rel_ca_p(self):
        return (self.vol_ca() * 9) / (self.vol_p() * 31)

    def osmolaridade(self):
        return ((self.vol_aac() * 0.8 + self.vol_glic() * 3.5 + self.vol_na() * 6.8 + self.vol_p() * 6.2)
                * 1000 / self.volume_total_npt()) - 50

    # Volume of ABD to complete the solution
    def vol_abd(self):
        return (self.volume_calculo() * self.fc) - (self.vol_glic() + self.vol_aac() + self.vol_lip() +
                                                    self.vol_ca() + self.vol_na() + self.vol_k() + self.vol_mg() + self.vol_p() + self.v_total_vit(
                    self.vol_vit()) +
                                                    self.vol_oligo())

    def volume_total_npt(self):
        return self.vol_glic() + self.vol_aac() + self.vol_lip() + \
            self.vol_ca() + self.vol_na() + self.vol_k() + self.vol_mg() + self.vol_p() + self.v_total_vit(
                self.vol_vit()) + \
            self.vol_oligo() + self.vol_abd()

    def vol_infusao(self):
        return self.volume_total_npt() / self.fc

    def mlh(self):
        return self.vol_infusao() / 24

    def to_json(self):
        return json.dumps({
            'peso': self.peso,
            'volume': self.volume,
            'vig': self.vig,
            'aac': self.aac,
            'lip': self.lip,
            'glicose_50': round(self.vol_glic(), 1),
            'proteinas': round(self.vol_aac(), 1),
            'lipidios': round(self.vol_lip(), 1),
            'abd': round(self.vol_abd(), 1),
            'ca': round(self.vol_ca(), 1),
            'na': round(self.vol_na(), 1),
            'k': round(self.vol_k(), 1),
            'mg': round(self.vol_mg(), 1),
            'p': round(self.vol_p(), 1),
            'oligoelementos': round(self.vol_oligo(), 1),
            'vitaminas': self.vol_vit(),
            'kcal_glic': round(self.kcal_glic(), 1),
            'kcal_prot': round(self.kcal_aac(), 1),
            'kcal_lip': round(self.kcal_lip(), 1),
            'kcal_nao_proteicas': round(self.kcal_nao_proteicas(), 1),
            'oferta_calorica_total': round(self.oferta_calorica_total(), 1),
            'total_cations': round(self.total_cations(), 1),
            'total_ca': round(self.total_ca(), 1),
            'rel_ca_p': round(self.rel_ca_p(), 1),
            'total_n': round(self.total_n(), 1),
            'osmolaridade': round(self.osmolaridade()),
            'volume_total': round(self.volume_total_npt(), 1),
            'volume_infusao': round(self.vol_infusao(), 1),
            'mlh': round(self.mlh(), 1)
        }
    )
