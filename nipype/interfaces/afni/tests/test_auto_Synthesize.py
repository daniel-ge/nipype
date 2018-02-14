# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import Synthesize


def test_Synthesize_inputs():
    input_map = dict(
        TR=dict(argstr='-TR %f', ),
        args=dict(argstr='%s', ),
        cbucket=dict(
            argstr='-cbucket %s',
            copyfile=False,
            mandatory=True,
        ),
        cenfill=dict(argstr='-cenfill %s', ),
        dry_run=dict(argstr='-dry', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        matrix=dict(
            argstr='-matrix %s',
            copyfile=False,
            mandatory=True,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_template='syn',
        ),
        outputtype=dict(),
        select=dict(
            argstr='-select %s',
            mandatory=True,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = Synthesize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Synthesize_outputs():
    output_map = dict(out_file=dict(), )
    outputs = Synthesize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
