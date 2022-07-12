#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on July 12, 2022, at 11:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'conditions2loopnew'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='allconditions1loop.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "c1odd" ---
ROLO = sound.Sound('ROLO20.wav', secs=-1, stereo=True, hamming=True,
    name='ROLO')
ROLO.setVolume(1.0)

# --- Initialize components for Routine "c1even" ---
RCLC = sound.Sound('RCLC20.wav', secs=-1, stereo=True, hamming=True,
    name='RCLC')
RCLC.setVolume(1.0)

# --- Initialize components for Routine "c2odd" ---
ROLC = sound.Sound('ROLC20.wav', secs=-1, stereo=True, hamming=True,
    name='ROLC')
ROLC.setVolume(1.0)

# --- Initialize components for Routine "c2even" ---
RCLO = sound.Sound('RCLO20.wav', secs=-1, stereo=True, hamming=True,
    name='RCLO')
RCLO.setVolume(1.0)

# --- Initialize components for Routine "c3odd" ---
RCLO2 = sound.Sound('RCLO20.wav', secs=-1, stereo=True, hamming=True,
    name='RCLO2')
RCLO2.setVolume(1.0)

# --- Initialize components for Routine "c4even" ---
ROLC2 = sound.Sound('ROLC20.wav', secs=-1, stereo=True, hamming=True,
    name='ROLC2')
ROLC2.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
Loop10 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Loop10')
thisExp.addLoop(Loop10)  # add the loop to the experiment
thisLoop10 = Loop10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop10.rgb)
if thisLoop10 != None:
    for paramName in thisLoop10:
        exec('{} = thisLoop10[paramName]'.format(paramName))

for thisLoop10 in Loop10:
    currentLoop = Loop10
    # abbreviate parameter names if possible (e.g. rgb = thisLoop10.rgb)
    if thisLoop10 != None:
        for paramName in thisLoop10:
            exec('{} = thisLoop10[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "c1odd" ---
    continueRoutine = True
    # update component parameters for each repeat
    ROLO.setSound('ROLO20.wav', secs=20.0, hamming=True)
    ROLO.setVolume(1.0, log=False)
    # keep track of which components have finished
    c1oddComponents = [ROLO]
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
    frameN = -1
    
    # --- Run Routine "c1odd" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLO
        if ROLO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLO.frameNStart = frameN  # exact frame index
            ROLO.tStart = t  # local t and not account for scr refresh
            ROLO.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('ROLO.started', tThisFlipGlobal)
            ROLO.play(when=win)  # sync with win flip
        if ROLO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLO.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLO.tStop = t  # not accounting for scr refresh
                ROLO.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ROLO.stopped')
                ROLO.stop()
        
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
    
    # --- Ending Routine "c1odd" ---
    for thisComponent in c1oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLO.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "c1even" ---
    continueRoutine = True
    # update component parameters for each repeat
    RCLC.setSound('RCLC20.wav', secs=20.0, hamming=True)
    RCLC.setVolume(1.0, log=False)
    # keep track of which components have finished
    c1evenComponents = [RCLC]
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
    frameN = -1
    
    # --- Run Routine "c1even" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLC
        if RCLC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLC.frameNStart = frameN  # exact frame index
            RCLC.tStart = t  # local t and not account for scr refresh
            RCLC.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('RCLC.started', tThisFlipGlobal)
            RCLC.play(when=win)  # sync with win flip
        if RCLC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLC.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLC.tStop = t  # not accounting for scr refresh
                RCLC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RCLC.stopped')
                RCLC.stop()
        
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
    
    # --- Ending Routine "c1even" ---
    for thisComponent in c1evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLC.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "c2odd" ---
    continueRoutine = True
    # update component parameters for each repeat
    ROLC.setSound('ROLC20.wav', secs=20.0, hamming=True)
    ROLC.setVolume(1.0, log=False)
    # keep track of which components have finished
    c2oddComponents = [ROLC]
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
    frameN = -1
    
    # --- Run Routine "c2odd" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLC
        if ROLC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLC.frameNStart = frameN  # exact frame index
            ROLC.tStart = t  # local t and not account for scr refresh
            ROLC.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('ROLC.started', tThisFlipGlobal)
            ROLC.play(when=win)  # sync with win flip
        if ROLC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLC.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLC.tStop = t  # not accounting for scr refresh
                ROLC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ROLC.stopped')
                ROLC.stop()
        
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
    
    # --- Ending Routine "c2odd" ---
    for thisComponent in c2oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLC.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "c2even" ---
    continueRoutine = True
    # update component parameters for each repeat
    RCLO.setSound('RCLO20.wav', secs=20.0, hamming=True)
    RCLO.setVolume(1.0, log=False)
    # keep track of which components have finished
    c2evenComponents = [RCLO]
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
    frameN = -1
    
    # --- Run Routine "c2even" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLO
        if RCLO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLO.frameNStart = frameN  # exact frame index
            RCLO.tStart = t  # local t and not account for scr refresh
            RCLO.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('RCLO.started', tThisFlipGlobal)
            RCLO.play(when=win)  # sync with win flip
        if RCLO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLO.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLO.tStop = t  # not accounting for scr refresh
                RCLO.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RCLO.stopped')
                RCLO.stop()
        
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
    
    # --- Ending Routine "c2even" ---
    for thisComponent in c2evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLO.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "c3odd" ---
    continueRoutine = True
    # update component parameters for each repeat
    RCLO2.setSound('RCLO20.wav', secs=20.0, hamming=True)
    RCLO2.setVolume(1.0, log=False)
    # keep track of which components have finished
    c3oddComponents = [RCLO2]
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
    frameN = -1
    
    # --- Run Routine "c3odd" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop RCLO2
        if RCLO2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RCLO2.frameNStart = frameN  # exact frame index
            RCLO2.tStart = t  # local t and not account for scr refresh
            RCLO2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('RCLO2.started', tThisFlipGlobal)
            RCLO2.play(when=win)  # sync with win flip
        if RCLO2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RCLO2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                RCLO2.tStop = t  # not accounting for scr refresh
                RCLO2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RCLO2.stopped')
                RCLO2.stop()
        
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
    
    # --- Ending Routine "c3odd" ---
    for thisComponent in c3oddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RCLO2.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "c4even" ---
    continueRoutine = True
    # update component parameters for each repeat
    ROLC2.setSound('ROLC20.wav', secs=20.0, hamming=True)
    ROLC2.setVolume(1.0, log=False)
    # keep track of which components have finished
    c4evenComponents = [ROLC2]
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
    frameN = -1
    
    # --- Run Routine "c4even" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ROLC2
        if ROLC2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ROLC2.frameNStart = frameN  # exact frame index
            ROLC2.tStart = t  # local t and not account for scr refresh
            ROLC2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('ROLC2.started', tThisFlipGlobal)
            ROLC2.play(when=win)  # sync with win flip
        if ROLC2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ROLC2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                ROLC2.tStop = t  # not accounting for scr refresh
                ROLC2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ROLC2.stopped')
                ROLC2.stop()
        
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
    
    # --- Ending Routine "c4even" ---
    for thisComponent in c4evenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ROLC2.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-20.000000)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'Loop10'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
