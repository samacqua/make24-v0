from gym.envs.registration import register

register(
    id='make24-v0',
    entry_point='gym_make24.envs:Make24Env',
)
