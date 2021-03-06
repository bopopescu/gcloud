# Copyright 2014 Google Inc. All Rights Reserved.
"""Command for listing target VPN gateways."""
from googlecloudsdk.compute.lib import base_classes


class List(base_classes.RegionalLister):
  """List target VPN gateways."""

  # Placeholder to indicate that a detailed_help field exists and should
  # be set outside the class definition.
  detailed_help = None

  @property
  def service(self):
    return self.compute.targetVpnGateways

  @property
  def resource_type(self):
    return 'targetVpnGateways'


List.detailed_help = {
    'brief': 'List target VPN Gateways',
    'DESCRIPTION': """\
        *{command}* lists summary information for the target VPN Gateways
        in a project.  The ``--uri'' option can be used to display the
        URIs for the target VPN Gateways.
        """,
}
