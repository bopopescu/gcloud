# Copyright 2014 Google Inc. All Rights Reserved.
"""The super-group for the compute CLI."""
import argparse

from googlecloudsdk.calliope import base
from googlecloudsdk.compute.lib import utils
from googlecloudsdk.core import properties


DETAILED_HELP = {
    'brief': 'Read and manipulate Google Compute Engine resources',
}


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Compute(base.Group):
  """Read and manipulate Google Compute Engine resources."""
  detailed_help = DETAILED_HELP


  def Filter(self, context, args):
    api_version = 'v1'
    utils.SetResourceParamDefaults()
    utils.UpdateContextEndpointEntries(context, self.Http(), api_version,
                                      )


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class ComputeBeta(base.Group):
  """Read and manipulate Google Compute Engine resources."""
  detailed_help = DETAILED_HELP


  def Filter(self, context, args):
    utils.SetResourceParamDefaults()
    utils.UpdateContextEndpointEntries(context, self.Http(), api_version='beta',
                                      )
