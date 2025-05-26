# Nautobot Apps Views

We saw examples of [NautobotUIViewtSet](https://docs.nautobot.com/projects/core/en/stable/development/apps/api/views/nautobotuiviewset/) in [Day 67](../Day067_Nautobot_Views_2_Nautobot_UI_ViewSet/README.md). But *NautobotUIViewSet* was relatively new in Nautobot-land as it was introduced in Nautobot 1.4. 

Prior to `NautobotUIViewSet`, Application views were generally imported from [nautobot.apps.views](https://github.com/nautobot/nautobot/blob/develop/nautobot/apps/views.py) with `generic` views.

Similar to their `NautobotUIViewSet` cousin, `generic` view and their associated `mixins` are just as capable to handle common operations such as displaying lists, handling forms, and perform database operations. They are still used widely in the code base, it can still be advantage to use in certain scenarios. 

> [!TIP]
> We will use the term `generic` view to differentiate them from `NautobotUIVewSet`, but they are **NOT** the same as Django generic views. These views came from `nautobot.core.views`. We can also refer to them as `Nautobot Generic Views`. 

In today's challenge, we will dive deeper into the generic views. 

## Environment Setup

We will use a combination of [Scenario 2](../Lab_Setup/scenario_2_setup/README.md) lab, [https://demo.nautobot.com/](https://demo.nautobot.com/), and [Nautbot Documentation](https://docs.nautobot.com/projects/core/en/latest/user-guide/core-data-model/overview/introduction/) for today's challenge. 

```
$ cd nautobot
$ poetry shell
$ poetry install
$ invoke build
(be patient with this step)
$ invoke debug
(be patient with this step as well)
```

### Key Views in `nautobot.apps.views`

The full list of views can be gleaned from [views.py](https://github.com/nautobot/nautobot/blob/develop/nautobot/apps/views.py): 

```
from nautobot.core.views.generic import (
    BulkComponentCreateView,
    BulkCreateView,
    BulkDeleteView,
    BulkEditView,
    BulkImportView,  # 3.0 TODO: deprecated, will be removed in 3.0
    BulkRenameView,
    ComponentCreateView,
    GenericView,
    ObjectDeleteView,
    ObjectEditView,
    ObjectImportView,
    ObjectListView,
    ObjectView,
)
from nautobot.core.views.mixins import (
    AdminRequiredMixin,
    ContentTypePermissionRequiredMixin,
    GetReturnURLMixin,
    NautobotViewSetMixin,
    ObjectBulkCreateViewMixin,  # 3.0 TODO: deprecated, will be removed in 3.0
    ObjectBulkDestroyViewMixin,
    ObjectBulkUpdateViewMixin,
    ObjectChangeLogViewMixin,
    ObjectDestroyViewMixin,
    ObjectDetailViewMixin,
    ObjectEditViewMixin,
    ObjectListViewMixin,
    ObjectNotesViewMixin,
    ObjectPermissionRequiredMixin,
)
```

Some common views are listed below, for more detail reference, check out [nautobot.apps.views code reference](https://docs.nautobot.com/projects/core/en/stable/code-reference/nautobot/apps/views/): 

1. **ObjectView**: Displays detailed information about a single object.
2. **ObjectListView**: Displays a list of objects.
3. **ObjectEditView**: Handles the edit of a single object.
4. **ObjectDeleteView**: Handles the deletion of a single objects.
6. **BulkCreateView**: Handles the bulk create of multiple objects.
6. **BulkEditView**: Handles the bulk edit of multiple objects.
7. **BulkDeleteView**: Handles the bulk deletion of multiple objects.

### Example: Using ObjectEditView

Let's try to trace one of the generic views. We can take a look at [Circuits App views.py](https://github.com/nautobot/nautobot/blob/develop/nautobot/circuits/views.py ): 

```python
...
from nautobot.core.views import generic, mixins as view_mixins
...

class CircuitSwapTerminations(generic.ObjectEditView):
    """
    Swap the A and Z terminations of a circuit.
    """

    queryset = Circuit.objects.all()

    def get(self, request, *args, **kwargs):
        circuit = get_object_or_404(self.queryset, pk=kwargs["pk"])
        form = ConfirmationForm()

        # Circuit must have at least one termination to swap
        if not circuit.circuit_termination_a and not circuit.circuit_termination_z:
            messages.error(
                request,
                f"No terminations have been defined for circuit {circuit}.",
            )
            return redirect("circuits:circuit", pk=circuit.pk)

        return render(
            request,
            "circuits/circuit_terminations_swap.html",
            {
                "circuit": circuit,
                "circuit_termination_a": circuit.circuit_termination_a,
                "circuit_termination_z": circuit.circuit_termination_z,
                "form": form,
                "panel_class": "default",
                "button_class": "primary",
                "return_url": circuit.get_absolute_url(),
            },
        )

    def post(self, request, *args, **kwargs):
        circuit = get_object_or_404(self.queryset, pk=kwargs["pk"])
        form = ConfirmationForm(request.POST)

        if form.is_valid():
            circuit_termination_a = CircuitTermination.objects.filter(
                circuit=circuit, term_side=CircuitTerminationSideChoices.SIDE_A
            ).first()
            circuit_termination_z = CircuitTermination.objects.filter(
                circuit=circuit, term_side=CircuitTerminationSideChoices.SIDE_Z
            ).first()

            if circuit_termination_a and circuit_termination_z:
                # Use a placeholder to avoid an IntegrityError on the (circuit, term_side) unique constraint
                with transaction.atomic():
                    circuit_termination_a.term_side = "_"
                    circuit_termination_a.save()
                    circuit_termination_z.term_side = "A"
                    circuit_termination_z.save()
                    circuit_termination_a.term_side = "Z"
                    circuit_termination_a.save()
            elif circuit_termination_a:
                circuit_termination_a.term_side = "Z"
                circuit_termination_a.save()
            else:
                circuit_termination_z.term_side = "A"
                circuit_termination_z.save()

            messages.success(request, f"Swapped terminations for circuit {circuit}.")
            return redirect("circuits:circuit", pk=circuit.pk)

        return render(
            request,
            "circuits/circuit_terminations_swap.html",
            {
                "circuit": circuit,
                "circuit_termination_a": circuit.circuit_termination_a,
                "circuit_termination_z": circuit.circuit_termination_z,
                "form": form,
                "panel_class": "default",
                "button_class": "primary",
                "return_url": circuit.get_absolute_url(),
            },
        )
```

Since we have not covered `form` yet, for now we can ignore some lines regarding Django forms. But we can already tell a few points from the code snippet: 

1. `CircuitSwapTerminations` is a class-based view inherited from `genericObjectEditView` for a single object. 
2. The `queryset` gets all the `Circuit` objects.
3. There are two supported HTTP methods, `get` and `post`.  
4. Each method performs operations and renders a response with templates under `cricuits` folder. 

As we move along with future challenges, keep in mind of the `views` we covered and reference back when needed. 

## Resources
- [Nautobot App Developer Guide Nautobot Generic Views](https://docs.nautobot.com/projects/core/en/stable/development/apps/api/views/nautobot-generic-views/)
- [Nautobot Core Developer Guide Generic Views](https://docs.nautobot.com/projects/core/en/stable/development/core/generic-views/)
- [nautobot.apps.views code reference](https://docs.nautobot.com/projects/core/en/stable/code-reference/nautobot/apps/views/)

## Day 68 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). 

Go ahead and give another example of Nautobot generic views in one of the apps for today's challenge on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will review what we have learned for Nautobot views. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+68+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 68 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 
