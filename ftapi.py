# @Author: shocquen

# Small wrapper for 42 api v2
# https://api.intra.42.fr/apidoc

import requests
from datetime import datetime
from enum import Enum
from typing import Optional, List, Any


class Kind(Enum):
    PEDAGOGY = "pedagogy"
    PROJECT = "project"
    SCOLARITY = "scolarity"
    SOCIAL = "social"


class Tier(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    NONE = "none"


class Achievement:
    id: int
    name: str
    description: str
    tier: Tier
    kind: Kind
    visible: bool
    image: str
    nbr_of_success: Optional[int]
    users_url: str

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        tier: Tier,
        kind: Kind,
        visible: bool,
        image: str,
        nbr_of_success: Optional[int],
        users_url: str,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.tier = tier
        self.kind = kind
        self.visible = visible
        self.image = image
        self.nbr_of_success = nbr_of_success
        self.users_url = users_url


class Language:
    id: int
    name: str
    identifier: str
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: int,
        name: str,
        identifier: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.name = name
        self.identifier = identifier
        self.created_at = created_at
        self.updated_at = updated_at


class Campus:
    id: int
    name: str
    time_zone: str
    language: Language
    users_count: int
    vogsphere_id: int
    country: str
    address: str
    zip: int
    city: str
    website: str
    facebook: str
    twitter: str
    active: bool
    public: bool
    email_extension: str
    default_hidden_phone: bool

    def __init__(
        self,
        id: int,
        name: str,
        time_zone: str,
        language: Language,
        users_count: int,
        vogsphere_id: int,
        country: str,
        address: str,
        zip: int,
        city: str,
        website: str,
        facebook: str,
        twitter: str,
        active: bool,
        public: bool,
        email_extension: str,
        default_hidden_phone: bool,
    ) -> None:
        self.id = id
        self.name = name
        self.time_zone = time_zone
        self.language = language
        self.users_count = users_count
        self.vogsphere_id = vogsphere_id
        self.country = country
        self.address = address
        self.zip = zip
        self.city = city
        self.website = website
        self.facebook = facebook
        self.twitter = twitter
        self.active = active
        self.public = public
        self.email_extension = email_extension
        self.default_hidden_phone = default_hidden_phone


class CampusUser:
    id: int
    user_id: int
    campus_id: int
    is_primary: bool
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: int,
        user_id: int,
        campus_id: int,
        is_primary: bool,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.campus_id = campus_id
        self.is_primary = is_primary
        self.created_at = created_at
        self.updated_at = updated_at


class Cursus:
    id: int
    created_at: datetime
    name: str
    slug: str
    kind: str

    def __init__(
        self, id: int, created_at: datetime, name: str, slug: str, kind: str
    ) -> None:
        self.id = id
        self.created_at = created_at
        self.name = name
        self.slug = slug
        self.kind = kind


class Skill:
    id: int
    name: str
    level: float

    def __init__(self, id: int, name: str, level: float) -> None:
        self.id = id
        self.name = name
        self.level = level


class Versions:
    large: str
    medium: str
    small: str
    micro: str

    def __init__(self, large: str, medium: str, small: str, micro: str) -> None:
        self.large = large
        self.medium = medium
        self.small = small
        self.micro = micro


class Image:
    link: str
    versions: Versions

    def __init__(self, link: str, versions: Versions) -> None:
        self.link = link
        self.versions = versions


class User:
    id: int
    email: str
    login: str
    first_name: str
    last_name: str
    usual_full_name: str
    usual_first_name: None
    url: str
    phone: str
    displayname: str
    kind: str
    image: Image
    staff: bool
    correction_point: int
    pool_month: str
    pool_year: int
    location: None
    wallet: int
    anonymize_date: datetime
    data_erasure_date: datetime
    created_at: datetime
    updated_at: datetime
    alumnized_at: None
    alumni: bool
    active: bool

    def __init__(
        self,
        id: int,
        email: str,
        login: str,
        first_name: str,
        last_name: str,
        usual_full_name: str,
        usual_first_name: None,
        url: str,
        phone: str,
        displayname: str,
        kind: str,
        image: Image,
        staff: bool,
        correction_point: int,
        pool_month: str,
        pool_year: int,
        location: None,
        wallet: int,
        anonymize_date: datetime,
        data_erasure_date: datetime,
        created_at: datetime,
        updated_at: datetime,
        alumnized_at: None,
        alumni: bool,
        active: bool,
    ) -> None:
        self.id = id
        self.email = email
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.usual_full_name = usual_full_name
        self.usual_first_name = usual_first_name
        self.url = url
        self.phone = phone
        self.displayname = displayname
        self.kind = kind
        self.image = image
        self.staff = staff
        self.correction_point = correction_point
        self.pool_month = pool_month
        self.pool_year = pool_year
        self.location = location
        self.wallet = wallet
        self.anonymize_date = anonymize_date
        self.data_erasure_date = data_erasure_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.alumnized_at = alumnized_at
        self.alumni = alumni
        self.active = active


class CursusUser:
    grade: Optional[str]
    level: float
    skills: List[Skill]
    blackholed_at: Optional[datetime]
    id: int
    begin_at: datetime
    end_at: Optional[datetime]
    cursus_id: int
    has_coalition: bool
    created_at: datetime
    updated_at: datetime
    user: User
    cursus: Cursus

    def __init__(
        self,
        grade: Optional[str],
        level: float,
        skills: List[Skill],
        blackholed_at: Optional[datetime],
        id: int,
        begin_at: datetime,
        end_at: Optional[datetime],
        cursus_id: int,
        has_coalition: bool,
        created_at: datetime,
        updated_at: datetime,
        user: User,
        cursus: Cursus,
    ) -> None:
        self.grade = grade
        self.level = level
        self.skills = skills
        self.blackholed_at = blackholed_at
        self.id = id
        self.begin_at = begin_at
        self.end_at = end_at
        self.cursus_id = cursus_id
        self.has_coalition = has_coalition
        self.created_at = created_at
        self.updated_at = updated_at
        self.user = user
        self.cursus = cursus


class ExpertisesUser:
    id: int
    expertise_id: int
    interested: bool
    value: int
    contact_me: bool
    created_at: datetime
    user_id: int

    def __init__(
        self,
        id: int,
        expertise_id: int,
        interested: bool,
        value: int,
        contact_me: bool,
        created_at: datetime,
        user_id: int,
    ) -> None:
        self.id = id
        self.expertise_id = expertise_id
        self.interested = interested
        self.value = value
        self.contact_me = contact_me
        self.created_at = created_at
        self.user_id = user_id


class Group:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class LanguagesUser:
    id: int
    language_id: int
    user_id: int
    position: int
    created_at: datetime

    def __init__(
        self,
        id: int,
        language_id: int,
        user_id: int,
        position: int,
        created_at: datetime,
    ) -> None:
        self.id = id
        self.language_id = language_id
        self.user_id = user_id
        self.position = position
        self.created_at = created_at


class Project:
    id: int
    name: str
    slug: str
    parent_id: Optional[int]

    def __init__(self, id: int, name: str, slug: str, parent_id: Optional[int]) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.parent_id = parent_id


class Status(Enum):
    FINISHED = "finished"
    PARENT = "parent"


class ProjectsUser:
    id: int
    occurrence: int
    final_mark: int
    status: Status
    validated: bool
    current_team_id: Optional[int]
    project: Project
    cursus_ids: List[int]
    marked_at: datetime
    marked: bool
    retriable_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: int,
        occurrence: int,
        final_mark: int,
        status: Status,
        validated: bool,
        current_team_id: Optional[int],
        project: Project,
        cursus_ids: List[int],
        marked_at: datetime,
        marked: bool,
        retriable_at: Optional[datetime],
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.occurrence = occurrence
        self.final_mark = final_mark
        self.status = status
        self.validated = validated
        self.current_team_id = current_team_id
        self.project = project
        self.cursus_ids = cursus_ids
        self.marked_at = marked_at
        self.marked = marked
        self.retriable_at = retriable_at
        self.created_at = created_at
        self.updated_at = updated_at


class TitlesUser:
    id: int
    user_id: int
    title_id: int
    selected: bool
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: int,
        user_id: int,
        title_id: int,
        selected: bool,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.title_id = title_id
        self.selected = selected
        self.created_at = created_at
        self.updated_at = updated_at


class User:
    id: int
    email: str
    login: str
    first_name: str
    last_name: str
    usual_full_name: str
    usual_first_name: None
    url: str
    phone: str
    displayname: str
    kind: str
    image: Image
    staff: bool
    correction_point: int
    pool_month: str
    pool_year: int
    location: None
    wallet: int
    anonymize_date: datetime
    data_erasure_date: datetime
    created_at: datetime
    updated_at: datetime
    alumnized_at: None
    alumni: bool
    active: bool
    groups: List[Group]
    cursus_users: List[CursusUser]
    projects_users: List[ProjectsUser]
    languages_users: List[LanguagesUser]
    achievements: List[Achievement]
    titles: List[Group]
    titles_users: List[TitlesUser]
    partnerships: List[Any]
    patroned: List[Any]
    patroning: List[Any]
    expertises_users: List[ExpertisesUser]
    roles: List[Any]
    campus: List[Campus]
    campus_users: List[CampusUser]

    def __init__(
        self,
        id: int,
        email: str,
        login: str,
        first_name: str,
        last_name: str,
        usual_full_name: str,
        usual_first_name: None,
        url: str,
        phone: str,
        displayname: str,
        kind: str,
        image: Image,
        staff: bool,
        correction_point: int,
        pool_month: str,
        pool_year: int,
        location: None,
        wallet: int,
        anonymize_date: datetime,
        data_erasure_date: datetime,
        created_at: datetime,
        updated_at: datetime,
        alumnized_at: None,
        alumni: bool,
        active: bool,
        groups: List[Group] or None,
        cursus_users: List[CursusUser] or None,
        projects_users: List[ProjectsUser] or None,
        languages_users: List[LanguagesUser] or None,
        achievements: List[Achievement] or None,
        titles: List[Group] or None,
        titles_users: List[TitlesUser] or None,
        partnerships: List[Any] or None,
        patroned: List[Any] or None,
        patroning: List[Any] or None,
        expertises_users: List[ExpertisesUser] or None,
        roles: List[Any] or None,
        campus: List[Campus] or None,
        campus_users: List[CampusUser] or None,
    ) -> None:
        self.id = id
        self.email = email
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.usual_full_name = usual_full_name
        self.usual_first_name = usual_first_name
        self.url = url
        self.phone = phone
        self.displayname = displayname
        self.kind = kind
        self.image = image
        self.staff = staff
        self.correction_point = correction_point
        self.pool_month = pool_month
        self.pool_year = pool_year
        self.location = location
        self.wallet = wallet
        self.anonymize_date = anonymize_date
        self.data_erasure_date = data_erasure_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.alumnized_at = alumnized_at
        self.alumni = alumni
        self.active = active
        self.groups = groups or None
        self.cursus_users = cursus_users or None
        self.projects_users = projects_users or None
        self.languages_users = languages_users or None
        self.achievements = achievements or None
        self.titles = titles or None
        self.titles_users = titles_users or None
        self.partnerships = partnerships or None
        self.patroned = patroned or None
        self.patroning = patroning or None
        self.expertises_users = expertises_users or None
        self.roles = roles or None
        self.campus = campus or None
        self.campus_users = campus_users or None


class FtClient:
    _id: str
    _secret: str
    _baseUrl: str = "https://api.intra.42.fr/v2/"
    _accessToken: str

    def __init__(self, id: str, secret: str) -> None:
        self._id = id
        self._secret = secret

    def getAccessToken(self) -> str:
        reqUrl = "https://api.intra.42.fr/oauth/token"
        headersList = {
            "Accept": "*/*",
            "User-Agent": "LLD (https://s.bde42.fr/discord)",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        form = {
            "grant_type": "client_credentials",
            "client_id": self._id,
            "client_secret": self._secret,
        }
        res = requests.request("POST", reqUrl, data=form, headers=headersList)
        return res.json()["access_token"]

    def setAccessToken(self) -> None:
        token = self.getAccessToken()
        self._accessToken = token

    def get(self, subPath: str) -> requests.Response:
        reqUrl = self._baseUrl + subPath
        headersList = {
            "Accept": "*/*",
            "User-Agent": "LLD (https://s.bde42.fr/discord)",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self._accessToken,
        }
        res = requests.request("GET", reqUrl, headers=headersList)
        return res

    def getUser(self, login: str) -> User:
        subPath = "users/" + login
        res = self.get(subPath=subPath)
        json = res.json()
        json["staff"] = json.pop("staff?")
        json["alumni"] = json.pop("alumni?")
        json["active"] = json.pop("active?")
        user = User(**json)
        return user

    def getUsers(self, logins: List[str]) -> List[User]:
        users = []
        subPath = "users?filter[login]="
        for login in logins:
            subPath += login + ","
        subPath = subPath[:-1]
        res = self.get(subPath=subPath)
        json = res.json()
        for userJson in json:
            userJson["staff"] = userJson.pop("staff?")
            userJson["alumni"] = userJson.pop("alumni?")
            userJson["active"] = userJson.pop("active?")
            user = User(
                **userJson,
                groups=None,
                cursus_users=None,
                projects_users=None,
                languages_users=None,
                achievements=None,
                titles=None,
                titles_users=None,
                partnerships=None,
                patroned=None,
                patroning=None,
                expertises_users=None,
                roles=None,
                campus=None,
                campus_users=None
            )
            users.append(user)
        return users
