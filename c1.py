#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 11, 2022, at 15:48
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
    originPath='c1.py',
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

# Initialize components for Routine "c1odd"
c1oddClock = core.Clock()
ROLO = sound.Sound('ROLO20.wav', secs=2.0, stereo=True, hamming=True,
    name='ROLO')
ROLO.setVolume(1.0)
filler1 = visual.TextStim(win=win, name='filler1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "c1even"
c1evenClock = core.Clock()
RCLC = sound.Sound('RCLC20.wav', secs=2.0, stereo=True, hamming=True,
    name='RCLC')
RCLC.setVolume(1.0)
filler2 = visual.TextStim(win=win, name='filler2',
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
loop1 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "c1odd"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    ROLO.setSound('ROLO20.wav', secs=2.0, hamming=True)
    ROLO.setVolume(1.0, log=False)
    # keep track of which components have finished
    c1oddComponents = [ROLO, filler1]
    for thisComponent in c1oddComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c1oddClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c1odd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c1oddClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c1oddClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLO
        if ROLO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLO.frameNStart = frameN  # exact frame index
            ROLO.tStart = t  # local t and not account for scr refresh
            ROLO.tStartRefresh = tThisFlipGlobal  # on global time
            ROLO.play(when=win)  # sync with win flip
        if ROLO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLO.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLO.tStop = t  # not accounting for scr refresh
                ROLO.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ROLO, 'tStopRefresh')  # time at next scr refresh
                ROLO.stop()
        
        # *filler1* updates
        if filler1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler1.frameNStart = frameN  # exact frame index
            filler1.tStart = t  # local t and not account for scr refresh
            filler1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler1, 'tStartRefresh')  # time at next scr refresh
            filler1.setAutoDraw(True)
        if filler1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler1.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler1.tStop = t  # not accounting for scr refresh
                filler1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler1, 'tStopRefresh')  # time at next scr refresh
                filler1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1oddComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c1odd"-------
    for thisComponent in c1oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLO.stop()  # ensure sound has stopped at end of routine
    loop1.addData('ROLO.started', ROLO.tStartRefresh)
    loop1.addData('ROLO.stopped', ROLO.tStopRefresh)
    loop1.addData('filler1.started', filler1.tStartRefresh)
    loop1.addData('filler1.stopped', filler1.tStopRefresh)
    
    # ------Prepare to start Routine "c1even"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    RCLC.setSound('RCLC20.wav', secs=2.0, hamming=True)
    RCLC.setVolume(1.0, log=False)
    # keep track of which components have finished
    c1evenComponents = [RCLC, filler2]
    for thisComponent in c1evenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c1evenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c1even"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c1evenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c1evenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLC
        if RCLC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLC.frameNStart = frameN  # exact frame index
            RCLC.tStart = t  # local t and not account for scr refresh
            RCLC.tStartRefresh = tThisFlipGlobal  # on global time
            RCLC.play(when=win)  # sync with win flip
        if RCLC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLC.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLC.tStop = t  # not accounting for scr refresh
                RCLC.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RCLC, 'tStopRefresh')  # time at next scr refresh
                RCLC.stop()
        
        # *filler2* updates
        if filler2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler2.frameNStart = frameN  # exact frame index
            filler2.tStart = t  # local t and not account for scr refresh
            filler2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler2, 'tStartRefresh')  # time at next scr refresh
            filler2.setAutoDraw(True)
        if filler2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                filler2.tStop = t  # not accounting for scr refresh
                filler2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler2, 'tStopRefresh')  # time at next scr refresh
                filler2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1evenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c1even"-------
    for thisComponent in c1evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLC.stop()  # ensure sound has stopped at end of routine
    loop1.addData('RCLC.started', RCLC.tStartRefresh)
    loop1.addData('RCLC.stopped', RCLC.tStopRefresh)
    loop1.addData('filler2.started', filler2.tStartRefresh)
    loop1.addData('filler2.stopped', filler2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'loop1'


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
