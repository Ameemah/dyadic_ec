#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 11, 2022, at 15:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.2.3')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'conditions2loopnew'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='c2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1707, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "operatorwait"
operatorwaitClock = core.Clock()
waitingforoperator = visual.TextStim(win=win, name='waitingforoperator',
    text='Waiting for operator',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
returnkey = keyboard.Keyboard()

# Initialize components for Routine "scannerwait"
scannerwaitClock = core.Clock()
tkey = keyboard.Keyboard()
waitingforscanner = visual.TextStim(win=win, name='waitingforscanner',
    text='Waiting for scanner',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "c2odd"
c2oddClock = core.Clock()
ROLC = sound.Sound('ROLC20.wav', secs=2.0, stereo=True, hamming=True,
    name='ROLC')
ROLC.setVolume(1.0)
filler3 = visual.TextStim(win=win, name='filler3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "c2even"
c2evenClock = core.Clock()
RCLO = sound.Sound('RCLO20.wav', secs=2.0, stereo=True, hamming=True,
    name='RCLO')
RCLO.setVolume(1.0)
filler4 = visual.TextStim(win=win, name='filler4',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "operatorwait"-------
continueRoutine = True
# update component parameters for each repeat
returnkey.keys = []
returnkey.rt = []
_returnkey_allKeys = []
# keep track of which components have finished
operatorwaitComponents = [waitingforoperator, returnkey]
for thisComponent in operatorwaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
operatorwaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "operatorwait"-------
while continueRoutine:
    # get current time
    t = operatorwaitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=operatorwaitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *waitingforoperator* updates
    if waitingforoperator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        waitingforoperator.frameNStart = frameN  # exact frame index
        waitingforoperator.tStart = t  # local t and not account for scr refresh
        waitingforoperator.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(waitingforoperator, 'tStartRefresh')  # time at next scr refresh
        waitingforoperator.setAutoDraw(True)
    
    # *returnkey* updates
    waitOnFlip = False
    if returnkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        returnkey.frameNStart = frameN  # exact frame index
        returnkey.tStart = t  # local t and not account for scr refresh
        returnkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(returnkey, 'tStartRefresh')  # time at next scr refresh
        returnkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(returnkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(returnkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if returnkey.status == STARTED and not waitOnFlip:
        theseKeys = returnkey.getKeys(keyList=['return'], waitRelease=False)
        _returnkey_allKeys.extend(theseKeys)
        if len(_returnkey_allKeys):
            returnkey.keys = _returnkey_allKeys[-1].name  # just the last key pressed
            returnkey.rt = _returnkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in operatorwaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "operatorwait"-------
for thisComponent in operatorwaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('waitingforoperator.started', waitingforoperator.tStartRefresh)
thisExp.addData('waitingforoperator.stopped', waitingforoperator.tStopRefresh)
# check responses
if returnkey.keys in ['', [], None]:  # No response was made
    returnkey.keys = None
thisExp.addData('returnkey.keys',returnkey.keys)
if returnkey.keys != None:  # we had a response
    thisExp.addData('returnkey.rt', returnkey.rt)
thisExp.addData('returnkey.started', returnkey.tStartRefresh)
thisExp.addData('returnkey.stopped', returnkey.tStopRefresh)
thisExp.nextEntry()
# the Routine "operatorwait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "scannerwait"-------
continueRoutine = True
# update component parameters for each repeat
tkey.keys = []
tkey.rt = []
_tkey_allKeys = []
# keep track of which components have finished
scannerwaitComponents = [tkey, waitingforscanner]
for thisComponent in scannerwaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
scannerwaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "scannerwait"-------
while continueRoutine:
    # get current time
    t = scannerwaitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=scannerwaitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tkey* updates
    waitOnFlip = False
    if tkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tkey.frameNStart = frameN  # exact frame index
        tkey.tStart = t  # local t and not account for scr refresh
        tkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tkey, 'tStartRefresh')  # time at next scr refresh
        tkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(tkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(tkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if tkey.status == STARTED and not waitOnFlip:
        theseKeys = tkey.getKeys(keyList=['t'], waitRelease=False)
        _tkey_allKeys.extend(theseKeys)
        if len(_tkey_allKeys):
            tkey.keys = _tkey_allKeys[-1].name  # just the last key pressed
            tkey.rt = _tkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *waitingforscanner* updates
    if waitingforscanner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        waitingforscanner.frameNStart = frameN  # exact frame index
        waitingforscanner.tStart = t  # local t and not account for scr refresh
        waitingforscanner.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(waitingforscanner, 'tStartRefresh')  # time at next scr refresh
        waitingforscanner.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scannerwaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scannerwait"-------
for thisComponent in scannerwaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if tkey.keys in ['', [], None]:  # No response was made
    tkey.keys = None
thisExp.addData('tkey.keys',tkey.keys)
if tkey.keys != None:  # we had a response
    thisExp.addData('tkey.rt', tkey.rt)
thisExp.addData('tkey.started', tkey.tStartRefresh)
thisExp.addData('tkey.stopped', tkey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('waitingforscanner.started', waitingforscanner.tStartRefresh)
thisExp.addData('waitingforscanner.stopped', waitingforscanner.tStopRefresh)
# the Routine "scannerwait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop2')
thisExp.addLoop(loop2)  # add the loop to the experiment
thisLoop2 = loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
if thisLoop2 != None:
    for paramName in thisLoop2:
        exec('{} = thisLoop2[paramName]'.format(paramName))

for thisLoop2 in loop2:
    currentLoop = loop2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
    if thisLoop2 != None:
        for paramName in thisLoop2:
            exec('{} = thisLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "c2odd"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    ROLC.setSound('ROLC20.wav', secs=2.0, hamming=True)
    ROLC.setVolume(1.0, log=False)
    # keep track of which components have finished
    c2oddComponents = [ROLC, filler3]
    for thisComponent in c2oddComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c2oddClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c2odd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c2oddClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c2oddClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLC
        if ROLC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLC.frameNStart = frameN  # exact frame index
            ROLC.tStart = t  # local t and not account for scr refresh
            ROLC.tStartRefresh = tThisFlipGlobal  # on global time
            ROLC.play(when=win)  # sync with win flip
        if ROLC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLC.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLC.tStop = t  # not accounting for scr refresh
                ROLC.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ROLC, 'tStopRefresh')  # time at next scr refresh
                ROLC.stop()
        
        # *filler3* updates
        if filler3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler3.frameNStart = frameN  # exact frame index
            filler3.tStart = t  # local t and not account for scr refresh
            filler3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler3, 'tStartRefresh')  # time at next scr refresh
            filler3.setAutoDraw(True)
        if filler3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler3.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler3.tStop = t  # not accounting for scr refresh
                filler3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler3, 'tStopRefresh')  # time at next scr refresh
                filler3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c2oddComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c2odd"-------
    for thisComponent in c2oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLC.stop()  # ensure sound has stopped at end of routine
    loop2.addData('ROLC.started', ROLC.tStartRefresh)
    loop2.addData('ROLC.stopped', ROLC.tStopRefresh)
    loop2.addData('filler3.started', filler3.tStartRefresh)
    loop2.addData('filler3.stopped', filler3.tStopRefresh)
    
    # ------Prepare to start Routine "c2even"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    RCLO.setSound('RCLO20.wav', secs=2.0, hamming=True)
    RCLO.setVolume(1.0, log=False)
    # keep track of which components have finished
    c2evenComponents = [RCLO, filler4]
    for thisComponent in c2evenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c2evenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c2even"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c2evenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c2evenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLO
        if RCLO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLO.frameNStart = frameN  # exact frame index
            RCLO.tStart = t  # local t and not account for scr refresh
            RCLO.tStartRefresh = tThisFlipGlobal  # on global time
            RCLO.play(when=win)  # sync with win flip
        if RCLO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLO.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLO.tStop = t  # not accounting for scr refresh
                RCLO.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RCLO, 'tStopRefresh')  # time at next scr refresh
                RCLO.stop()
        
        # *filler4* updates
        if filler4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler4.frameNStart = frameN  # exact frame index
            filler4.tStart = t  # local t and not account for scr refresh
            filler4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler4, 'tStartRefresh')  # time at next scr refresh
            filler4.setAutoDraw(True)
        if filler4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler4.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler4.tStop = t  # not accounting for scr refresh
                filler4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler4, 'tStopRefresh')  # time at next scr refresh
                filler4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c2evenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c2even"-------
    for thisComponent in c2evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLO.stop()  # ensure sound has stopped at end of routine
    loop2.addData('RCLO.started', RCLO.tStartRefresh)
    loop2.addData('RCLO.stopped', RCLO.tStopRefresh)
    loop2.addData('filler4.started', filler4.tStartRefresh)
    loop2.addData('filler4.stopped', filler4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'loop2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
