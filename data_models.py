from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


@dataclass
class SummaryGear:
    id: str
    resource_state: int
    primary: bool
    name: str
    distance: float


class ActivityType(Enum):
    AlpineSki = "AlpineSki"
    BackcountrySki = "BackcountrySki"
    Canoeing = "Canoeing"
    Crossfit = "Crossfit"
    EBikeRide = "EBikeRide"
    Elliptical = "Elliptical"
    Golf = "Golf"
    Handcycle = "Handcycle"
    Hike = "Hike"
    IceSkate = "IceSkate"
    InlineSkate = "InlineSkate"
    Kayaking = "Kayaking"
    Kitesurf = "Kitesurf"
    NordicSki = "NordicSki"
    Ride = "Ride"
    RockClimbing = "RockClimbing"
    RollerSki = "RollerSki"
    Rowing = "Rowing"
    Run = "Run"
    Sail = "Sail"
    Skateboard = "Skateboard"
    Snowboard = "Snowboard"
    Snowshoe = "Snowshoe"
    Soccer = "Soccer"
    StairStepper = "StairStepper"
    StandUpPaddling = "StandUpPaddling"
    Surfing = "Surfing"
    Swim = "Swim"
    Velomobile = "Velomobile"
    VirtualRide = "VirtualRide"
    VirtualRun = "VirtualRun"
    Walk = "Walk"
    WeightTraining = "WeightTraining"
    Wheelchair = "Wheelchair"
    Windsurf = "Windsurf"
    Workout = "Workout"
    Yoga = "Yoga"


@dataclass
class SummaryClub:
    id: int
    resource_state: int
    name: str
    profile_medium: str
    cover_photo: str
    cover_photo_small: str
    sport_type: str
    activity_types: List['ActivityType']
    city: str
    state: str
    country: str
    private: bool
    member_count: int
    featured: bool
    verified: bool
    url: str


@dataclass
class Athlete:
    username: str
    bio: str
    id: int
    badge_type_id: int
    friend: bool
    follower: bool
    blocked: bool
    can_follow: bool
    mutual_friend_count: int
    athlete_type: int
    date_preference: str
    is_winback_via_upload: bool
    is_winback_via_view: bool


    resource_state: int
    firstname: str
    lastname: str
    profile_medium: str
    profile: str
    city: str
    state: str
    country: str
    sex: str
    premium: bool
    summit: bool
    created_at: datetime
    updated_at: datetime
    follower_count: int
    friend_count: int
    measurement_preference: str
    ftp: int
    weight: float
    clubs: List['SummaryClub']
    bikes: List['SummaryGear']
    shoes: List['SummaryGear']
