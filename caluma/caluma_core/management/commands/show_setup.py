import textwrap

from django.conf import settings
from django.core.management.commands import migrate

from caluma.caluma_core import types as core_types
from caluma.caluma_core.visibilities import BaseVisibility


class Command(migrate.Command):
    """Show some setup details of this particular Caluma installation."""

    def _show_suppressable_visibilities(self):
        self.stdout.write(
            textwrap.dedent("""
            ## Suppressable visibility connections:

            On some connections, it does not make sense to invoke the visibility
            layer. To improve performance in these cases, you can suppress
            visibilities by setting `suppress_visibilities` in your visibility
            class(es).

            >>> class MyCustomVisibility(BaseVisibility):
            >>>     ...
            >>>     suppress_visibilities = [
            >>>         ...
            >>>     ]

            Possible values are shown below:
        """).strip()
        )

        for vis in sorted(BaseVisibility._suppressable_visibilities):
            self.stdout.write(f"* {vis}")

        collected_suppressors = set()
        for vis in core_types.Node.visibility_classes:
            collected_suppressors.update(vis.suppress_visibilities)

        self.stdout.write("\nThe following visibilities are currently suppressed:")
        for vis in sorted(collected_suppressors):
            self.stdout.write(f"* {vis}")
        if not collected_suppressors:
            print("(none)")

    def _show_configured_visibility_classes(self):
        self.stdout.write(
            textwrap.dedent("""
            ## Configured visibility classes

            The following classes are currently defined for the visibility
            layer:
        """).strip()
        )
        for cls in settings.VISIBILITY_CLASSES:
            self.stdout.write(f"* {cls}")

    def _show_configured_permission_classes(self):
        self.stdout.write(
            textwrap.dedent("""
            ## Configured permission classes

            The following classes are currently defined for the permission
            layer:
        """).strip()
        )
        for cls in settings.PERMISSION_CLASSES:
            self.stdout.write(f"* {cls}")

    def handle(self, *args, **options):
        self.stdout.write("# Caluma configuration environment")
        self.stdout.write("\n")
        self._show_configured_visibility_classes()
        self.stdout.write("\n\n")
        self._show_configured_permission_classes()
        self.stdout.write("\n\n")
        self._show_suppressable_visibilities()
