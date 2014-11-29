import logging

logger = logging.getLogger("grc.controllers.helpers.Qt")

'''
 Handles connecting signals from given actions to handlers
    self    - Calling class
    actions - Dictionary of a QAction and unique key

 Dynamically build the connections for the signals by finding the correct
 function to handle an action.

 Essentially the same as QMetaObject::connectSlotsByName, except the actions
  and slots can be separated into a view and controller class

'''

def connectSlots(self, actions):
    for key in actions:
        try:
            handler = key + "_clicked"
            actions[key].triggered.connect(getattr(self, handler))
            logger.debug("Action <%s> connected to handler <%s>" % (key, handler))
        except:
            # Just in case someone forgot
            try:
                logger.warning("Slot not implemented for signal <%s> in %s" % (key, type(self)))
                actions[key].triggered.connect(getattr(self, 'notImplemented'))
            except:
                logger.error("Class cannot handle signal for action <%s>" % key)
