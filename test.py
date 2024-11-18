from examples.example_2_branching_multistep.ex_2_model_classes import Trial, g, event_position_df
from vidigi.animation import animate_activity_log
import pandas as pd

g.arrival_df = "examples/example_2_branching_multistep/ed_arrivals.csv"

g.number_of_runs = 1

my_trial = Trial()
result = my_trial.run_trial()

fig = animate_activity_log(
        event_log=my_trial.all_event_logs[my_trial.all_event_logs['run']==1],
        event_position_df=event_position_df,
        scenario=g(),
        debug_mode=False,
        every_x_time_units=5,
        include_play_button=True,
        gap_between_entities=20,
        gap_between_rows=15,
        plotly_height=550,
        plotly_width=800,
        override_x_max=700,
        override_y_max=675,
        icon_and_text_size=12,
        wrap_queues_at=10,
        step_snapshot_max=50,
        limit_duration=g.sim_duration,
        time_display_units="dhm",
        display_stage_labels=False,
        #add_background_image="Full Model Background Image - Horizontal Layout.drawio.png",
        custom_entity_icon_list=["🔴"]
    )

fig
