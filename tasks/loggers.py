import pypline


@pypline.requires("trials")
class ParentLogger(pypline.Task):
    def process(self, message, pipeline):
        for i, trial in enumerate(message.trials):
            print "%i: (%i parents) %s" % (i, len(trial.parents), trial)
            for parent in trial.parents:
                print parent
        return message


@pypline.requires("best")
class TerminalLogger(pypline.Task):
    def process(self, message, pipeline):
        print "Generation: %s" % message.generation
        print "Best: %s" % message.best
        print "Fitness: %f" % message.best.fitness
        return message


@pypline.requires("initialisation")
class PercentRemainingLogger(pypline.Task):
    def process(self, message, pipeline):
        import sys
        print "\r%.1f%%..." % message.percent,
        sys.stdout.flush()
        return message
