#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 11, 2022, at 15:52
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
    originPath='c3.py',
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

# Initialize components for Routine "c3odd"
c3oddClock = core.Clock()
RCLO2 = sound.Sound('RCLO20.wav', secs=2.0, stereo=True, hamming=True,
    name='RCLO2')
RCLO2.setVolume(1.0)
filler5 = visual.TextStim(win=win, name='filler5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "c3even"
c3evenClock = core.Clock()
ROLC2 = sound.Sound('ROLC20.wav', secs=2.0, stereo=True, hamming=True,
    name='ROLC2')
ROLC2.setVolume(1.0)
filler6 = visual.TextStim(win=win, name='filler6',
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
loop3 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop3')
thisExp.addLoop(loop3)  # add the loop to the experiment
thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
if thisLoop3 != None:
    for paramName in thisLoop3:
        exec('{} = thisLoop3[paramName]'.format(paramName))

for thisLoop3 in loop3:
    currentLoop = loop3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
    if thisLoop3 != None:
        for paramName in thisLoop3:
            exec('{} = thisLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "c3odd"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    RCLO2.setSound('RCLO20.wav', secs=2.0, hamming=True)
    RCLO2.setVolume(1.0, log=False)
    # keep track of which components have finished
    c3oddComponents = [RCLO2, filler5]
    for thisComponent in c3oddComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c3oddClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c3odd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c3oddClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c3oddClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLO2
        if RCLO2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLO2.frameNStart = frameN  # exact frame index
            RCLO2.tStart = t  # local t and not account for scr refresh
            RCLO2.tStartRefresh = tThisFlipGlobal  # on global time
            RCLO2.play(when=win)  # sync with win flip
        if RCLO2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLO2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLO2.tStop = t  # not accounting for scr refresh
                RCLO2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RCLO2, 'tStopRefresh')  # time at next scr refresh
                RCLO2.stop()
        
        # *filler5* updates
        if filler5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler5.frameNStart = frameN  # exact frame index
            filler5.tStart = t  # local t and not account for scr refresh
            filler5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler5, 'tStartRefresh')  # time at next scr refresh
            filler5.setAutoDraw(True)
        if filler5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler5.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler5.tStop = t  # not accounting for scr refresh
                filler5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler5, 'tStopRefresh')  # time at next scr refresh
                filler5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c3oddComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c3odd"-------
    for thisComponent in c3oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLO2.stop()  # ensure sound has stopped at end of routine
    loop3.addData('RCLO2.started', RCLO2.tStartRefresh)
    loop3.addData('RCLO2.stopped', RCLO2.tStopRefresh)
    loop3.addData('filler5.started', filler5.tStartRefresh)
    loop3.addData('filler5.stopped', filler5.tStopRefresh)
    
    # ------Prepare to start Routine "c3even"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    ROLC2.setSound('ROLC20.wav', secs=2.0, hamming=True)
    ROLC2.setVolume(1.0, log=False)
    # keep track of which components have finished
    c3evenComponents = [ROLC2, filler6]
    for thisComponent in c3evenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c3evenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c3even"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c3evenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c3evenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLC2
        if ROLC2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLC2.frameNStart = frameN  # exact frame index
            ROLC2.tStart = t  # local t and not account for scr refresh
            ROLC2.tStartRefresh = tThisFlipGlobal  # on global time
            ROLC2.play(when=win)  # sync with win flip
        if ROLC2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLC2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLC2.tStop = t  # not accounting for scr refresh
                ROLC2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ROLC2, 'tStopRefresh')  # time at next scr refresh
                ROLC2.stop()
        
        # *filler6* updates
        if filler6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler6.frameNStart = frameN  # exact frame index
            filler6.tStart = t  # local t and not account for scr refresh
            filler6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler6, 'tStartRefresh')  # time at next scr refresh
            filler6.setAutoDraw(True)
        if filler6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler6.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler6.tStop = t  # not accounting for scr refresh
                filler6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler6, 'tStopRefresh')  # time at next scr refresh
                filler6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c3evenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c3even"-------
    for thisComponent in c3evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLC2.stop()  # ensure sound has stopped at end of routine
    loop3.addData('ROLC2.started', ROLC2.tStartRefresh)
    loop3.addData('ROLC2.stopped', ROLC2.tStopRefresh)
    loop3.addData('filler6.started', filler6.tStartRefresh)
    loop3.addData('filler6.stopped', filler6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'loop3'


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
