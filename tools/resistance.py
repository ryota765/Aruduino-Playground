class ResistanceCalculator:
    
    def series(self,resistance_list):
        return sum(resistance_list)

    def parallel(self,resistance_list):
        return 1/sum([1/resistance for resistance in resistance_list])