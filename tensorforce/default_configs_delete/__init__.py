# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


from tensorforce.default_configs.memory_agent import MemoryAgentConfig
from tensorforce.default_configs.dqn import DQNAgentConfig, DQNModelConfig
from tensorforce.default_configs.dqfd import DQFDAgentConfig
from tensorforce.default_configs.naf import NAFAgentConfig, NAFModelConfig
from tensorforce.default_configs.vpg import VPGAgentConfig, VPGModelConfig
from tensorforce.default_configs.trpo import TRPOAgentConfig, TRPOModelConfig

__all__ = [
    'MemoryAgentConfig',
    'DQNAgentConfig', 'DQNModelConfig',
    'DQFDAgentConfig',
    'NAFAgentConfig', 'NAFModelConfig',
    'VPGAgentConfig', 'VPGModelConfig',
    'TRPOAgentConfig', 'TRPOModelConfig'
]