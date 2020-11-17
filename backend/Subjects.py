class Subjects:
    
    def __init__(self):
        
        # static class id lookup table
        lookup = {

            101 : "Elementary Math",
            102 : "Algebra",
            103 : "Geometry",
            104 : "Trigonometry",
            105 : "Pre-Calculus",
            107 : "Calculus",
            106 : "Statistics",
            
            201 : "Biology",
            202 : "Chemistry",
            203 : "Physics",
            204 : "Physiology",

            301 : "Paper Development and Organization",
            302 : "Proofreading",
            303 : "Finding Sources and Citing",
            304 : "College Essay Help",

            401 : "Beginner Coding",

            501 : "Historical Analysis",
            502 : "Writing Historical Papers",

            601 : "Beginner to Advanced French",
            602 : "Beginner Spanish",
            603 : "Arabic",

            701 : "Study/Organization Skills",
            702 : "Adobe Creative Suite",
            703 : "Resume/Cover Letter Help",
            704 : "Interview Prep",
            705 : "Leadership Development",

            801 : "SAT Prep",
            802 : "ACT Prep"
            
        }

        self.active = []

    def getClassName(self, id):
        return self.lookup[id]
        