from siriObjects.baseObjects import AceObject, ClientBoundCommand, ServerBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView, Snippet
from siriObjects.systemObjects import DomainObject


class ClockAdd(ClientBoundCommand):
    def __init__(self):
        super(ClockAdd, self).__init__("Add", "com.apple.ace.clock")
        self.clockToAdd = None # ClockObject
        self.targetAppId = None #url

    def to_plist(self):
        self.add_property('clockToAdd')
        self.add_property('targetAppId')
        return super(ClockAdd, self).to_plist()

class ClockAddCompleted(ServerBoundCommand):
    classIdentifier = "AddCompleted"
    groupIdentifier = "com.apple.ace.clock"
    def __init__(self, plist):
        self.worldClockId = None #url
        self.alreadyExists = None # bool
        super(ClockAddCompleted, self).__init__(plist)

class ClockDelete(ClientBoundCommand):
    def __init__(self):
        super(ClockDelete, self).__init__("Delete", "com.apple.ace.clock")
        self.clockIds = None # array
        self.targetAppId = None # url

    def to_plist(self):
        self.add_property('clockIds')
        self.add_property('targetAppId')
        return super(ClockDelete, self).to_plist()

class ClockDeleteCompleted(ServerBoundCommand):
    classIdentifier = "DeleteCompleted"
    groupIdentifier = "com.apple.ace.clock"
    def __init__(self, plist):
        super(ClockDeleteCompleted, self).__init__(plist)


class ClockObject(DomainObject):
    def __init__(self):
        super(ClockObject, self).__init__("com.apple.ace.clock")
        self.unlocalizedCountryName = None
        self.unlocalizedCityName = None
        self.timezoneId = None
        self.countryName = None
        self.countryCode = None
        self.cityName = None
        self.alCityId = None
    
    def to_plist(self):
        self.add_property('unlocalizedCountryName')
        self.add_property('unlocalizedCityName')
        self.add_property('timezoneId') 
        self.add_property('countryName')
        self.add_property('countryCode')
        self.add_property('cityName')
        self.add_property('alCityId')
        return super(ClockObject, self).to_plist()

class ClockSearch(ClientBoundCommand):
    def __init__(self):
        self.unlocalizedCountryName = None # string 
        self.unlocalizedCityName = None # string
        self.identifier = None #url
        self.countryCode = None # string
        self.alCityId = None # number
        self.targetAppId = None # url
    
    def to_plist(self):
        self.add_property('unlocalizedCountryName')
        self.add_property('unlocalizedCityName')
        self.add_property('identifier')
    	self.add_property('countryCode')
        self.add_property('alCityId')
    	self.add_property('targetAppId')
        return super(ClockSearch, self).to_plist()

class ClockSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.ace.apple.clock"
    def __init__(self, plist):
        self.results = None # array
        super(ClockSearchCompleted, self).__init__(plist)
    
class ClockSnippet(Snippet):
    def __init__(self, clocks=None):
        super(ClockSnippet, self).__init__("com.apple.ace.clock")
        self.clocks = clocks if clocks != None else []
    
    def to_plist(self):
        self.add_property('clocks')
        return super(ClockSnippet, self).to_plist()