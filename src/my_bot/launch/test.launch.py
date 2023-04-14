import launch
import launch.actions
import launch.substitutions



def generate_launch_description():
    #to launch one launch file from other
    first_launch_file = launch.substitutions.LaunchConfiguration('launch_sim', default='/home/maneesh/dev_ws/src/my_bot/launch/launch_sim.launch.py')
    first_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(first_launch_file),
        launch_arguments={'world': './src/my_bot/worlds/house.world'}.items()
    )

    # Define the command to launch slam_toolbox
    slam_toolbox_cmd = [
        'ros2', 'launch', 'slam_toolbox', 'online_async_launch.py',
        'params_file:=./src/my_bot/config/mapper_params_online_async.yaml',
        'use_sim_time:=true'
    ]
    # Define the command to launch nav2_bringup
    nav2_bringup_cmd = [
        'ros2', 'launch', 'nav2_bringup', 'bringup_launch.py',
        'use_sim_time:=true',
        'params_file:=./src/my_bot/config/nav2_params.yaml',
        'map:=/home/user/map.yaml'
    ]

    # Define the ExecuteProcess actions to launch the commands
    slam_toolbox_execute_process = launch.actions.ExecuteProcess(
        cmd=slam_toolbox_cmd,
        output='screen'
    )
    nav2_bringup_execute_process = launch.actions.ExecuteProcess(
        cmd=nav2_bringup_cmd,
        output='screen'
    )
    # second_launch_file = launch.substitutions.LaunchConfiguration('finial', default='/home/maneesh/dev_ws/src/my_bot/launch/finial.launch.py')
    # second_launch = launch.actions.IncludeLaunchDescription(
    #     launch.launch_description_sources.PythonLaunchDescriptionSource(second_launch_file),
        
    # )


    # Create the launch description with the ExecuteProcess actions
    ld = launch.LaunchDescription()
    ld.add_action(slam_toolbox_execute_process)
    ld.add_action(nav2_bringup_execute_process)
    ld.add_action(first_launch)
    # ld.add_action(second_launch)
    return ld
