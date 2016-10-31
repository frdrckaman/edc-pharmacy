from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.test import TestCase

from edc_pharma.choices import TABLET
from edc_pharma.forms.dispense_form import DispenseForm
from edc_pharma.tests.factories.factory import SiteFactory, PatientFactory, ProtocolFactory,\
    MedicationFactory, DispenseFactory


class TestDispenseModel(TestCase):
    """Setup data with all required fields for DISPENSE TYPE: IV"""
    def setUp(self):
        self.protocol = ProtocolFactory()
        self.site = SiteFactory()
        self.patient = PatientFactory()
        self.medication = MedicationFactory()
        self.dispense = DispenseFactory(patient=self.patient, medication=self.medication)
        self.data = {
            'patient': self.patient.id,
            'medication': self.medication.id,
            'dispense_type': TABLET,
            'number_of_tablets': 1,
            'total_number_of_tablets': 30,
            'syrup_dose': None,
            'total_dosage_volume': None,
            'iv_duration': None,
            'times_per_day': 1,
            'concentration': None,
            'prepared_date': date.today(),
            'prepared_datetime': datetime.now()}

    def test_refill_date_logic(self):
        """Test to verify whether the refill date method returns the right date"""
        self.assertEqual(self.dispense.refill_date, date.today() + relativedelta(days=16))

    def test_unique_date_medication_patient(self):
        """Test to verify that unique integrity in fields: patient, medication, prepared_date is maintained"""
        form = DispenseForm(data=self.data)
        self.assertFalse(form.is_valid())
