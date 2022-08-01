#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on July 28, 2022, at 17:13
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
    originPath='1loopexp.py',
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

# Initialize components for Routine "startexp"
startexpClock = core.Clock()
key = keyboard.Keyboard()
waitingforscanner = visual.TextStim(win=win, name='waitingforscanner',
    text='Waiting for scanner',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "c1odd"
if participant == one:
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
if participant == one:
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

# Initialize components for Routine "c2odd"
if participant == two:
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
if participant == two:
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

# Initialize components for Routine "c3odd"
if participant == three:
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

# Initialize components for Routine "c4even"
if participant = three:
    c4evenClock = core.Clock()
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

# ------Prepare to start Routine "startexp"-------
continueRoutine = True
# update component parameters for each repeat
key.keys = []
key.rt = []
_key_allKeys = []
# keep track of which components have finished
startexpComponents = [key, waitingforscanner]
for thisComponent in startexpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startexpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startexp"-------
while continueRoutine:
    # get current time
    t = startexpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startexpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key* updates
    waitOnFlip = False
    if key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key.frameNStart = frameN  # exact frame index
        key.tStart = t  # local t and not account for scr refresh
        key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key, 'tStartRefresh')  # time at next scr refresh
        key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key.status == STARTED and not waitOnFlip:
        theseKeys = key.getKeys(keyList=['t'], waitRelease=False)
        _key_allKeys.extend(theseKeys)
        if len(_key_allKeys):
            key.keys = _key_allKeys[-1].name  # just the last key pressed
            key.rt = _key_allKeys[-1].rt
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
    for thisComponent in startexpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startexp"-------
for thisComponent in startexpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key.keys in ['', [], None]:  # No response was made
    key.keys = None
thisExp.addData('key.keys',key.keys)
if key.keys != None:  # we had a response
    thisExp.addData('key.rt', key.rt)
thisExp.addData('key.started', key.tStartRefresh)
thisExp.addData('key.stopped', key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('waitingforscanner.started', waitingforscanner.tStartRefresh)
thisExp.addData('waitingforscanner.stopped', waitingforscanner.tStopRefresh)
# the Routine "startexp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/khana/Downloads/1loopexp (1).xlsx'),
    seed=None, name='Loop')
thisExp.addLoop(Loop)  # add the loop to the experiment
thisLoop = Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in Loop:
    currentLoop = Loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
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
    Loop.addData('ROLO.started', ROLO.tStartRefresh)
    Loop.addData('ROLO.stopped', ROLO.tStopRefresh)
    Loop.addData('filler1.started', filler1.tStartRefresh)
    Loop.addData('filler1.stopped', filler1.tStopRefresh)
    
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
    Loop.addData('RCLC.started', RCLC.tStartRefresh)
    Loop.addData('RCLC.stopped', RCLC.tStopRefresh)
    Loop.addData('filler2.started', filler2.tStartRefresh)
    Loop.addData('filler2.stopped', filler2.tStopRefresh)
    
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
    Loop.addData('ROLC.started', ROLC.tStartRefresh)
    Loop.addData('ROLC.stopped', ROLC.tStopRefresh)
    Loop.addData('filler3.started', filler3.tStartRefresh)
    Loop.addData('filler3.stopped', filler3.tStopRefresh)
    
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
    Loop.addData('RCLO.started', RCLO.tStartRefresh)
    Loop.addData('RCLO.stopped', RCLO.tStopRefresh)
    Loop.addData('filler4.started', filler4.tStartRefresh)
    Loop.addData('filler4.stopped', filler4.tStopRefresh)
    
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
    Loop.addData('RCLO2.started', RCLO2.tStartRefresh)
    Loop.addData('RCLO2.stopped', RCLO2.tStopRefresh)
    Loop.addData('filler5.started', filler5.tStartRefresh)
    Loop.addData('filler5.stopped', filler5.tStopRefresh)
    
    # ------Prepare to start Routine "c4even"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    ROLC2.setSound('ROLC20.wav', secs=2.0, hamming=True)
    ROLC2.setVolume(1.0, log=False)
    # keep track of which components have finished
    c4evenComponents = [ROLC2, filler6]
    for thisComponent in c4evenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    c4evenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "c4even"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = c4evenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=c4evenClock)
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
        for thisComponent in c4evenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "c4even"-------
    for thisComponent in c4evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLC2.stop()  # ensure sound has stopped at end of routine
    Loop.addData('ROLC2.started', ROLC2.tStartRefresh)
    Loop.addData('ROLC2.stopped', ROLC2.tStopRefresh)
    Loop.addData('filler6.started', filler6.tStartRefresh)
    Loop.addData('filler6.stopped', filler6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'Loop'


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
