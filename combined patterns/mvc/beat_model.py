from abc import ABC, abstractmethod




class BeatModelInterface(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def setBPM(self, bpm):
        pass

    @abstractmethod
    def register_observer(self, obs:BeatObserver):
        pass

    @abstractmethod
    def remove_observer(self, obs:BeatObserver):
        pass

    @abstractmethod
    def register_observer(self, obs:BPMObserver):
        pass

    @abstractmethod
    def remove_observer(self, obs:BPMObserver):
        pass


class BeatModel(BeatModelInterface):

    def __init__(self):
        self.sequencer = None
        self._beatObservers = []
        self._bpmObservers = []
        self.bpm = 90


    def initialize(self):
        self.set_up_midi()
        self.build_track_and_start()

    def on(self):
        self.sequencer.start()
        self.setBPM(90)

    def off(self):
        self.setBPM(0)
        self.sequencer.stop()

    def setBPM(self, bpm):
        self.bpm = bpm
        self.sequencer.setTempInBPM(self.getBPM())

    def getBPM(self):
        return self.bpm

    def beatEvent(self):
        pass





