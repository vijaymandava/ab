
This folder has a set of File-based LIMS request and cancel files.
The intent is to identify what parts of File-based LIMS specification the Instrument supports, and what the Simulator supports.
The specification identifies (4) ways to Order/Cancel.

More specifically, the goal is to identify:
a) what the physical instrument supports for File-based LIMS (i.e. identify bugs Instrument to Specification)
b) what the simulator supports for File-based LIMS (i.e. identify bugs Simulator)

With above analysis we will now know what subset of File-based LIMS that we can use for testing.

For details on the "cases" below, and File-based LIMS specification:
 JAMA GDP-VER-3952 Auto-Cancel 01 - Overview
 RND0058 Rev A

Overview:

Case 0  = RND0058-A 2.2.1   Order/Cancel using LIMS ID, M/AA/HR
Case 1  = RND0058-A 2.2.1.1 Order/Cancel using LIMS ID, Sample ID
Case 2  = RND0058-A 2.2.2   Order/Cancel using Serial Number, M/AA/HR
Case 2b =                   Order/Cancel using LIMS ID, Serial Number, M/AA/HR
Case 3  = RND0058-A 2.2.3   Order/Cancel using Sample ID, Lot/Batch

Observations:

Case 0:
instrument works per specification
simulator performs Order correctly.
---> simulator does not load (there is no Serial Number)
---> simulator does not cancel properly - it requires m/aa/hr where instrument and spec do not.
this means the simulator can be used to order and cancel, with a workaround.  Cannot load/run test.

Case 1:
instrument works per specification
simulator performs Order correctly.
---> simulator does not load (there is no Serial Number)
simulator cancels properly - this case has LIMS_ID and Sample_ID

Case 2:
instrument works per specification
simulator performs Order correctly
simulator loads (there is Serial Number)
simulator cancels properly - this case hasserial number only (no LIMS ID)

Case 2b:  (this is technically not in the specification - we do this for testing purposes - both Serial Number and LIMS_ID)


