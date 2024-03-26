from ....test.bases import WorldTestBase
from .. import locations


class ToontownTestBase(WorldTestBase):
    game = "Toontown"


class ToontownTestDefault(ToontownTestBase):
    pass


class ToontownTestPlaygroundAccess(ToontownTestBase):

    def test_playground_access(self):

        # TTC always available
        for i in range(12):
            self.assertTrue(self.can_reach_location(f"Toontown Central Task #{i + 1}"))

        # Test task + clearance working correctly
        for pg_name in ("Donald's Dock", "Daisy Gardens", "Minnie's Melodyland", "The Brrrgh", "Donald's Dreamland"):

            for i in range(12):
                self.assertFalse(self.can_reach_location(f"{pg_name} Task #{i + 1}"))

            self.collect_by_name([f"{pg_name} HQ Clearance"])

            for i in range(12):
                self.assertTrue(self.can_reach_location(f"{pg_name} Task #{i + 1}"))


class TestFacilityAccess(ToontownTestBase):
    def test_facility_access(self):
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_FRONT_FACTORY.value], [["Front Factory Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_SIDE_FACTORY.value], [["Side Factory Key"]])

        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_COIN_MINT.value], [["Coin Mint Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_DOLLAR_MINT.value], [["Dollar Mint Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_BULLION_MINT.value], [["Bullion Mint Key"]])

        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_A_OFFICE.value], [["A Office Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_B_OFFICE.value], [["B Office Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_C_OFFICE.value], [["C Office Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_D_OFFICE.value], [["D Office Key"]])

        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_FRONT_ONE.value], [["Front One Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_MIDDLE_TWO.value], [["Middle Two Key"]])
        self.assertAccessDependency([locations.ToontownLocationName.CLEAR_BACK_THREE.value], [["Back Three Key"]])

class TestBossAccess(ToontownTestBase):

    def test_boss_access(self):
        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.SELLBOT_PROOF.value))
        self.collect_by_name(["Sellbot Disguise"])
        self.assertTrue(self.can_reach_location(locations.ToontownLocationName.SELLBOT_PROOF.value))

        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.CASHBOT_PROOF.value))
        self.collect_by_name(["Cashbot Disguise"])
        self.assertTrue(self.can_reach_location(locations.ToontownLocationName.CASHBOT_PROOF.value))

        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.LAWBOT_PROOF.value))
        self.collect_by_name(["Lawbot Disguise"])
        self.assertTrue(self.can_reach_location(locations.ToontownLocationName.LAWBOT_PROOF.value))

        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.BOSSBOT_PROOF.value))
        self.collect_by_name(["Bossbot Disguise"])
        self.assertTrue(self.can_reach_location(locations.ToontownLocationName.BOSSBOT_PROOF.value))

    def test_victory_condition(self):

        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.value))
        self.collect_by_name(["Sellbot Disguise"])
        self.collect_by_name(["Sellbot Proof"])
        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.value))
        self.collect_by_name(["Cashbot Proof"])
        self.collect_by_name(["Cashbot Disguise"])
        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.value))
        self.collect_by_name(["Lawbot Proof"])
        self.collect_by_name(["Lawbot Disguise"])
        self.assertFalse(self.can_reach_location(locations.ToontownLocationName.value))
        self.collect_by_name(["Bossbot Proof"])
        self.collect_by_name(["Bossbot Disguise"])

        self.assertTrue(self.can_reach_location(locations.ToontownLocationName.value))
