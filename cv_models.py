from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: date
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    location: Optional[str] = None
    description: Optional[str] = None

class WorkExperience(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    location: Optional[str] = None
    description: List[str] = Field(default_factory=list)
    achievements: Optional[List[str]] = None
    technologies: Optional[List[str]] = None

class Project(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: Optional[date] = None
    technologies: List[str]
    role: Optional[str] = None
    url: Optional[str] = None
    achievements: Optional[List[str]] = None

class Skill(BaseModel):
    category: str
    items: List[str]

class Language(BaseModel):
    name: str
    proficiency: str
    certification: Optional[str] = None

class Certification(BaseModel):
    name: str
    issuer: str
    date_obtained: date
    expiration_date: Optional[date] = None
    credential_id: Optional[str] = None
    url: Optional[str] = None

class ContactInformation(BaseModel):
    full_name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None

class CV(BaseModel):
    contact: ContactInformation
    summary: str
    education: List[Education]
    work_experience: List[WorkExperience] = None
    projects: Optional[List[Project]] = None
    skills: List[Skill]
    languages: Optional[List[Language]] = None
    certifications: Optional[List[Certification]] = None
    interests: Optional[List[str]] = None
    references: Optional[List[str]] = None 