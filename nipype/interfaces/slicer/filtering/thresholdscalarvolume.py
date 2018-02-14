# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class ThresholdScalarVolumeInputSpec(CommandLineInputSpec):
    InputVolume = File(
        position=-2, desc="Input volume", exists=True, argstr="%s")
    OutputVolume = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Thresholded input volume",
        argstr="%s")
    threshold = traits.Int(desc="Threshold value", argstr="--threshold %d")
    lower = traits.Int(desc="Lower threshold value", argstr="--lower %d")
    upper = traits.Int(desc="Upper threshold value", argstr="--upper %d")
    outsidevalue = traits.Int(
        desc=
        "Set the voxels to this value if they fall outside the threshold range",
        argstr="--outsidevalue %d")
    thresholdtype = traits.Enum(
        "Below",
        "Above",
        "Outside",
        desc=
        "What kind of threshold to perform. If Outside is selected, uses Upper and Lower values. If Below is selected, uses the ThresholdValue, if Above is selected, uses the ThresholdValue.",
        argstr="--thresholdtype %s")


class ThresholdScalarVolumeOutputSpec(TraitedSpec):
    OutputVolume = File(
        position=-1, desc="Thresholded input volume", exists=True)


class ThresholdScalarVolume(SEMLikeCommandLine):
    """title: Threshold Scalar Volume

category: Filtering

description: <p>Threshold an image.</p><p>Set image values to a user-specified outside value if they are below, above, or between simple threshold values.</p><p>ThresholdAbove: The values greater than or equal to the threshold value are set to OutsideValue.</p><p>ThresholdBelow: The values less than or equal to the threshold value are set to OutsideValue.</p><p>ThresholdOutside: The values outside the range Lower-Upper are set to OutsideValue.</p><p>Although all image types are supported on input, only signed types are produced.</p><p>

version: 0.1.0.$Revision: 2104 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Threshold

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = ThresholdScalarVolumeInputSpec
    output_spec = ThresholdScalarVolumeOutputSpec
    _cmd = "ThresholdScalarVolume "
    _outputs_filenames = {'OutputVolume': 'OutputVolume.nii'}
